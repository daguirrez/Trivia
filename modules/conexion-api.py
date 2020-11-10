#Script que trae las preguntas de la api Open Trivia DB

import requests

def get_trivia_data(categoria, dificultad, tipo):

    urlapi = "https://opentdb.com/api.php?amount=10"
    # Formato de url: &category=27&difficulty=easy&type=multiple

    trivia_category = {
        '1' : '9', #General Knowledge
        '2' : '10', #Books
        '3' : '11', #Films
        '4' : '12', #Music
        '5' : '15', #Video Games
        '6' : '26', #Celebrities
        '7' : '27', #Animals
        '8' : '29', #Comics
        '9' : '31', #Anime
        '10' : '32' #Cartoon
    }
    
    category = trivia_category.get(str(categoria))

    urlapic = urlapi + "&category=" + str(category)

    trivia_difficulty = {
        '1' : 'easy',
        '2' : 'medium',
        '3' : 'hard'
    }

    difficulty = trivia_difficulty.get(str(dificultad))
    
    urlapicd = urlapic + "&difficulty=" + difficulty
    
    trivia_type = {
        '1' : 'multiple',
        '2' : 'boolean'
    }

    types = trivia_type.get(str(tipo))
    
    urlapifull = urlapicd + "&type=" + types

    response = requests.get(urlapifull)
    data = response.json()

    if data['response_code'] != 0:
        if data['response_code'] == 1:
            return "No hay suficientes preguntas en la BD para generar tu trivia"
        if data['response_code'] == 2:
            return "Hay un parametro erroneo"
    
    questions = data['results']

    return questions

def main():

    #si deberia funcionar
    preguntas = get_trivia_data(3, 1, 2)
    print (preguntas)

    print()

    #no hay suficientes preguntas en la BD
    preguntas2 = get_trivia_data(3, 2, 2)
    print(preguntas2)

    print()

    #Parametro erroneo
    preguntas3 = get_trivia_data(42, 3, 1)
    print(preguntas3)

if __name__ == '__main__':
    main()
