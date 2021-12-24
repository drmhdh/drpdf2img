class Translation(object):
    START_TEXT = """Hello <i><b>{}</b></i>,
I Can rename ✍ with custom thumbnail and upload as video/file
Type /help for more details."""
    DOWNLOAD_START_VIDEO = "Downloading Video to my server.....📥"
    DOWNLOAD_START = "Downloading File to my server.....📥"
    UPLOAD_START_VIDEO = "Uploading as video.....📤"
    UPLOAD_START = "Uploading as File.....📤"
    RCHD_TG_API_LIMIT = "Downloaded in {} seconds.\nDetected File Size: {}\nSorry.\nBut, I cannot upload files greater than 1.95GB due to Telegram API limitations.I can't do anything for that 🤷‍♂️."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "📄 Done"
    AFTER_SUCCESSFUL_UPLOAD_MSG_VIDEO = "🎞 Done"
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "📥 {} seconds.\n📤 {} seconds."
    SAVED_CUSTOM_THUMB_NAIL = "Custom File thumbnail saved ✅️ .\nThis image will be deleted with in 24hr🗑"
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅ Custom thumbnail cleared succesfully."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully. ✅"
    SAVED_RECVD_DOC_FILE_VIDEO = "Video Downloaded Successfully. ✅"
    CUSTOM_CAPTION_UL_FILE = ""
    NO_CUSTOM_THUMB_NAIL_FOUND = "❓ No Custom ThumbNail found."
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    HELP_USER = """Hai <b><i>{}</i></b>, 
1. Send Me A Thumbnail.
2. Send me the file to be Renamed.
3. Reply to that message with <code>/rename new name.extension</code>. with custom thumbnail support.\n(upload as file)
4. Reply to that message with <code>/rename_video new name.extension</code>. with custom thumbnail support.\n(uploading as Video)
5. Send <code>/deletethumbnail</code> for deleting saved thumbnail
"""
    REPLY_TO_DOC_FOR_RENAME_FILE = "🤦‍♂️ Reply to a Telegram media to `/rename New Name.extension` with custom thumbnail support.\n\n(For uploading as file).\n\nSee /help for more information. "
    REPLY_TO_DOC_FOR_RENAME_VIDEO = "🤦‍♂ Reply to a Telegram media to `/rename_video New Name.extension` with custom thumbnail support.\n\n(For uploading as video).\n\nSee /help for more information."
    IFLONG_FILE_NAME = """File Name limit allowed by Telegram is {alimit} characters.
The given file name has {num} characters.
<b>Essays Not allowed in Telegram file name!</b>
Please short your file name and try again!"""
