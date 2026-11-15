
from pathlib import Path
from playwright.sync_api import sync_playwright

USERNAME = "SAROJGMG"
SERVER_ID = "654317"

URL = f"https://topg.org/minecraft-servers/server-{SERVER_ID}#vote"
PROFILE_DIR = str(Path(__file__).parent / ".topg_browser")


def main():
    with sync_playwright() as p:
        context = p.chromium.launch_persistent_context(
            user_data_dir=PROFILE_DIR,
            headless=False,
            viewport={"width": 1280, "height": 900}
        )

        page = context.pages[0] if context.pages else context.new_page()

        print("Opening TopG voting page...")
        page.goto(URL, wait_until="domcontentloaded", timeout=60000)

        print(f"Server: {SERVER_ID}")
        print(f"Minecraft username: {USERNAME}")
        print("\nComplete the voting process manually.")
        print("Log in if required and complete any verification.")
        print("Press ENTER here when finished.")

        input()

        print("Closing browser...")
        context.close()


if __name__ == "__main__":
    main()
