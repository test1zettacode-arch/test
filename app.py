from fastapi.responses import RedirectResponse



async def red():
    return RedirectResponse(url=f"https://zettadevelop.ru/index?user_id={}", 303)