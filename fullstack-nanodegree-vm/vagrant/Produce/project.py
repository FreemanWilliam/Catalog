from flask import Flask
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Produce, ProduceItem

engine = create_engine('sqlite:///producemenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route('/')
@app.route('/produce')
def Produce():
	
	test = session.query(Produce).all()
	s = ''
	
	for i in test:		
		s+='</br>'
		s+=str(i.id)
		'''
		s+='</br>'
		s+=str(i.id)
		s+='</br>'
		s+=str(i.description)
		s+='</br>'
		s+=str(i.price)
		s+='</br>'
		s+=str(i.type)
		s+='</br>'
		s+=str(i.produce_id)
			'''
	output = s
	
	
	return output
		   


if __name__ == '__main__':	

	app.run(host = '0.0.0.0', port = 8080)
	app.debug = True