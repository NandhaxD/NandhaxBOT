
import config 
import traceback

def cb_wrapper(func):
    async def wrapper(client, cb):
        users = await get_all_pros()
        if cb.from_user.id in config.OWNER_ID:
            await cb.answer(
                "You cannot access this!",
                cache_time=0,
                show_alert=True,
            )
        else:
            try:
                await func(client, cb)
            except MessageNotModified:
                await cb.answer("🤔🧐")
            except Exception as e:
                print(traceback.format_exc())
                await cb.answer(
                    f"Oh No, SomeThing Isn't Right. Please Check Logs!",
                    cache_time=0,
                    show_alert=True,
                )

    return wrapper
