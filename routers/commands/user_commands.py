import csv
import io


from aiogram import Router, types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils import markdown


router=Router(name=__name__)


@router.message(Command("code", prefix="/!%"))
async def handle_command_code(message: types.Message):
    text = markdown.text(
        "Here's Python code:",
        "",

        markdown.markdown_decoration.pre_language(
            markdown.text(
                "print('Hello world!)",
            "\n",
            "def foo():\n    return 'bar'",
            sep="\n",
            ),
            language="python",

        ),
        "And here's some JS:",
        "",
        markdown.markdown_decoration.pre_language(
            markdown.text(
                "console.log('Hello world')",
                "\n",
                "function foo() {\n  return 'bar'\n}",
            sep="\n",
            ),
            language="javascript",
        ),
        sep="\n",
    )
    await message.answer(text=text, parse_mode=ParseMode.MARKDOWN_V2)


@router.message(Command("picture"))
async def handle_command_pic(message: types.Message):
    url = 'https://flomaster.top/o/uploads/posts/2023-10/thumbs/1698061198_flomaster-top-p-prikolnie-nebolshie-legkie-risunki-vkontak-2.jpg'

    await message.reply_photo(
        photo=url,
        caption="egg",
    )


@router.message(Command("csv"))
async def send_txt_file(message: types.Message):
    file = io.StringIO()
    csv_writer = csv.writer(file)
    csv_writer.writerows([
        ["Name", "Age", "City"],
        ["John Smith", "28", "New York"],

        ])
    await message.reply_document(
        document=types.BufferedInputFile(
            file=file.getvalue().encode(("utf-8")),
            filename="people.csv",
        )

    )
