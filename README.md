# AirBnB clone - The console

## Desciption 
AirBnB clone is a featuring database storage, a back-end API, and front-end interfacing in a clone of AirBnB. The project currently implements the back-end console.


## Classes 🆑
HolbertonBnB utilizes the following classes:
- BaseModel
- FileStorage
- User
- State
- City
- Amenity
- Place
- Review

### PUBLIC INSTANCE ATTRIBUTES
- id
- created_at
- updated_at


### PUBLIC INSTANCE METHODS
- save
- to_dict
- all
- new
- save
- reload

### PUBLIC CLASS ATTRIBUTES
- email
- password
- first_name
- last_name
- name
- state_id
- name
- city_id
- user_id
- name
- description
- number_rooms
- number_bathrooms
- max_guest
- price_by_night
- latitude
- longitude
- amenity_ids
- place_id
- user_id
- text

### PRIVATE CLASS ATTRIBUTES
- file_path
- objects

## Storage 🛄
The above classes are managed by the abstracted storage engine defined in the FileStorage class. The storage object is loaded/re-loaded from the JSON file file.json as class instances are created, updated, or deleted.

## Console 💻
The console is a command-line interpreter for managing the backend of HolbertonBnB. It can handle and manipulate all classes utilized by the application through calls on the storage object defined above.

## Console Commands
The HBNB console supports the following commands:
- create
- show
- destory
- all
- count
- update

## Testing 📏
Unittests for the HolbertonBnB project are defined in the tests folder. To run the entire test suite simultaneously, execute the following command:
```bash
$ python3 -m unittest discover tests
```
## Authors ✒️
- NAZIH TOUIH (NEAZYIT)
- diri smitk HHHHHHHHHHH
