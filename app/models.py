from . import db

class Property(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    bedrooms = db.Column(db.Integer)
    bathrooms = db.Column(db.Integer)
    price = db.Column(db.Float)
    location = db.Column(db.String(255))
    type = db.Column(db.String(255))
    description = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    
    
    def __init__(self, title, bedrooms, bathrooms, price, location, type, description, photo):
        self.title = title
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.location = location
        self.type = type
        self.description = description
        self.photo = photo

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support    
   
        
    def __repr__(self):
        return f'<Property {self.title}>'
