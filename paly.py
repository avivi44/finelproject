import sys

# קבלת מספר כפרמטר
number = sys.argv[1]

# בדיקה האם פלינדרום
if number == number[::-1]:
    result = f"✅ The number {number} is a palindrome."
    status = "green"
else:
    result = f"❌ The number {number} is NOT a palindrome."
    status = "red"

# כתיבת התוצאה לקובץ HTML
with open("output.html", "w") as f:
    f.write("<html><body>")
    f.write("<h1>Palindrome Check</h1>")
    f.write(f"<p><strong>Number:</strong> {number}</p>")
    f.write(f"<p style='color:{status};'>{result}</p>")
    f.write("</body></html>")

print(result)
