import qr_code as qr
img = qr("https://studio.youtube.com/channel/UCD8SGFDHcI8a_toBqE6otUw/videos/upload?filter=%5B%5D&sort=%7B%22columnType%22%3A%22date%22%2C%22sortOrder%22%3A%22DESCENDING%22%7D")
img.save("faheem_wadipora.png")