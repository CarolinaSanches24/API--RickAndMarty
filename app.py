from flask import Flask, render_template,  jsonify
import urllib.request, json

app = Flask (__name__)

@app.route("/") # rota de  URL raiz
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character";
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read(); # leitura dos dados vindos da api
    dict = json.loads(data); # transforma esses dados em json p/ python
    
    return render_template("personagens.html", characters = dict["results"])

@app.route("/profile/<id>") # obter um personagem

def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/"+id;
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    dict = json.loads(data);
    
    return render_template("profile.html", profile = dict)

@app.route("/lista")

def get_list_characters():
    url = "https://rickandmortyapi.com/api/character";
    response = urllib.request.urlopen(url)
    characters = response.read();
    dict = json.loads(characters);
    
    characters = []
    
    for character in dict["results"]:
        character = {
            "name":character["name"],
            "status":character["status"]
        }
        
        characters.append(character);
    return {"characters":characters}

@app.route("/locations") # rota de locations
def get_list_locations_page():
    url = "https://rickandmortyapi.com/api/location";
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read(); # leitura dos dados vindos da api
    dict = json.loads(data); # transforma esses dados em json p/ python
    
    return render_template("locations.html", locations = dict["results"]);
   
     
@app.route("/listalocations") # rota da lista de localizações
def get_locations():
    url = "https://rickandmortyapi.com/api/location";
    response = urllib.request.urlopen(url) # envia a req e recebe a res
    data = response.read(); # leitura dos dados vindos da api
    dict = json.loads(data); # transforma esses dados em json p/ python
    
    locations = [];
    
    for location in dict["results"]:
        location = {
            "id":location["id"],
            "name":location["name"],
            "type":location["type"],
            "dimension":location["dimension"],
        }
        
        locations.append(location);
    
    return {"locations":locations}

@app.route("/location/<id>") # obter uma location
def get_location(id):
    url = f"https://rickandmortyapi.com/api/location/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    location_dict = json.loads(data);
    list_ids = [];
    character_names = [];
    
    for resident in location_dict["residents"]:
        resident_id = resident.split("/")[-1]
        list_ids.append(resident_id);
        
        # Consulta o nome do personagem pelo id e armazena na lista
        character_url = f"https://rickandmortyapi.com/api/character/{resident_id}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        character_names.append(character_dict["name"])
        
    residents_info = list(zip(list_ids, character_names))
        
    return render_template("location.html", location=location_dict, residents_info = residents_info);

# Listar Episodios
@app.route("/episodes")
def get_list_episodes():
    url = "https://rickandmortyapi.com/api/episode";
    response = urllib.request.urlopen(url) 
    data = response.read();
    episodes_dict = json.loads(data); 
    
    episodes = [];
    
    for episode in episodes_dict["results"]:
        episode = {
            "id":episode["id"],
            "name":episode["name"],
            "air_date":episode["air_date"],
            "episode":episode["episode"]
        }
        episodes.append(episode);
        
    return render_template("episodes.html", episodes=episodes);

@app.route("/episode/<id>") # obter uma location
def get_episode(id):
    url = f"https://rickandmortyapi.com/api/episode/{id}"
    response = urllib.request.urlopen(url) 
    data = response.read(); 
    episode_dict = json.loads(data);
    list_ids_characters = [];
    character_names = [];
    
    for character in episode_dict["characters"]:
        character_id = character.split("/")[-1]
        list_ids_characters.append(character_id);
        
        # Consulta o nome do personagem pelo id e armazena na lista
        character_url = f"https://rickandmortyapi.com/api/character/{character_id}"
        character_response = urllib.request.urlopen(character_url)
        character_data = character_response.read()
        character_dict = json.loads(character_data)
        character_names.append(character_dict["name"])
        
        
        # characters_info = list(zip(list_ids_characters, character_names))
        
    return render_template("episode.html", episode=episode_dict, list_ids_characters = list_ids_characters, characters_names = character_names);