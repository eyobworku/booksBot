from gemini import Gemini

# "__Secure-1PSIDCC" : "AKEyXzX2fuxszVVltLD6EveHDsJiy1eX8N7sQEBDL2Dfn9RrpkCVa3hVRfd_srQnQSP9GC6AF0w",
cookies = {
    "__Secure-1PSID": "g.a000jQiDrHLz0BH9i-1qtJiVB9Jvkcyu-J9oH9Qx2_Z6MTUhoVleNdCqrN7yPUmyXm7RxbdiEwACgYKASUSAQASFQHGX2MiNN1a36fGxmE-mNTwk7M4cxoVAUF8yKqrPAzewOWCy263ZWwpnooX0076",
    "__Secure-1PSIDTS": "sidts-CjIBLwcBXBRQ11webR2Q8ccHiHhuTNpgNBWRAxQXswywdDjsyv2bD0vxMSPxTTUhFfSgUhAA",
}
client = Gemini(cookies=cookies)

response = client.generate_content(
    "are you are not gemini"
)
print(response.payload)
