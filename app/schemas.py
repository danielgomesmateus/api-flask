from flask_restful import fields

contact_field = {
    "name": fields.String,
    "cellphone": fields.String
}

user_field = {
    "username": fields.String,
    "password": fields.String
}
