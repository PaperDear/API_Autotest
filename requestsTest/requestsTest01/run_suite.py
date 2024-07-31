import jsonschema

schema = {
    "type": "array"
}

data =(1,2,3)

print(jsonschema.validate(list(data), schema))
