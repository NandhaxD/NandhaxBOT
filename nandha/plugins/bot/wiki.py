


from nandha import bot
from pyrogram import filters, types, enums


from bs4 import BeautifulSoup
import requests
import json


def fetch_wikipedia_search_results(query, limit=5):
    url = f"https://en.m.wikipedia.org/w/index.php?search={query}&title=Special%3ASearch&profile=advanced&fulltext=1&ns0=1"
    response = requests.get(url)
    
    if response.status_code != 200:
        print("Error fetching the page")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')

    results = []

    # Check if there are search results
    no_results_tag = soup.find('p', class_='mw-search-nonefound')
    if no_results_tag:
        return results

    # Extract the search results
    search_results = soup.find_all('div', class_='mw-search-result-heading')
    descriptions = soup.find_all('div', class_='searchresult')

    for i in range(min(limit, len(search_results))):
        title_tag = search_results[i].find('a')
        if title_tag:
            title = title_tag.get('title')
            url = "https://en.wikipedia.org" + title_tag.get('href')
            description = descriptions[i].get_text(strip=True) if i < len(descriptions) else ""
            results.append({
                'title': title,
                'description': description,
                'url': url
            })
    return results



@bot.on_message(filters.command("wiki"))
async def wiki(client, message):
    if len(message.command) == 1:
        return await message.reply(
           "What do you want to search?"
        )
    query = ' '.join(message.command[1:])
    search_results = fetch_wikipedia_search_results(query)
    if not search_results:
        await message.reply_text("No results found.")
        return

    buttons = [
        [InlineKeyboardButton(result['title'], callback_data=f"wiki:{json.dumps(result)}")] for result in search_results
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text("Choose a result:", reply_markup=reply_markup)

# Function to handle callback queries
@bot.on_callback_query(filters.regex('^wiki'))
async def button(client, query):
    result = json.loads(query.data.split(":", 1)[1])
  
    message = f"{result['title']}\n\n{result['description']}\n\nURL: {result['url']}"
    await query.edit_message_text(text=message)
