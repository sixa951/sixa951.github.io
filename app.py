from ext import app

if __name__ == '__main__':
    from routes import home,register,help,contact,product,login,sale
app.run(debug=True)
