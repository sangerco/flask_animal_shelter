from models import Pet, db
from app import app

db.drop_all()
db.create_all()

sparkles = Pet(name = 'Sparkles', species = 'cat', photo_url = 'https://images.pexels.com/photos/259803/pexels-photo-259803.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=500', age = '1', notes = '')
rowdy = Pet(name = 'Rowdy', species = 'dog', photo_url = 'https://i2-prod.mirror.co.uk/incoming/article22588506.ece/ALTERNATES/s615/0_Dogs-Trust.jpg', age = '7', notes='good boy')
natasha = Pet(name = 'Natasha', species = 'porcupine', photo_url='https://images.unsplash.com/photo-1605369179590-014a88d4560a?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8cG9yY3VwaW5lfGVufDB8fDB8fA%3D%3D&w=1000&q=80', age = '1', notes='given up for adoption')
fred = Pet(name='Fred', species='dog', age='5', available=False)

db.session.add_all([sparkles, rowdy, natasha, fred])
db.session.commit()