# Telegram Bot to convert any document to PDF and To Merge Files to Pdf.

- I recommend you to use python 3.10.11

```python
pip install -r requirements.txt
```

```python
python main.py
```

The bot use the [CloudConvert](https://cloudconvert.com/apis/file-conversion) API. So you need to grab your API key. CloudConvert give only `10 points` in `free` account.

Add `.env` file and include `BOT_TOKEN` for telegram key and `API_KEY` for cloudconvert APY Key.

Send any `File` to convert it to `Pdf`
![ConvertionDemo](https://i.imgur.com/NpMFg18.gif)

To merge send /merge command and send the files when finished click Done. You can send a text to set a custom name
