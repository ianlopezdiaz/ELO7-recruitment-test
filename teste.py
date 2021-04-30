"""
Ainda não há nada implementado aqui. Apenas um esqueleto de script.
"""


import sys

def print_help():
    help_string = """
    Usage:
        python teste.py --category "{'feature_1':<input_da_feature_1>,'feature_2':<input_da_feature_2>,...}"
        python teste.py --intent "<termo_de_busca_do_usuário>"
        python teste.py --help
    """
    print(helt_string)

def category(features_dict):
    return features_dict

def intent(user_query):
    return user_query

def recommendation(user_query):
    return user_query


if __name__ == '__main__':
    if len(sys.argv) == 3:
        if sys.argv[1] == '--category':
            features_dict = eval(sys.argv[2])
            if type(features_dict) == dict:
                print(category(features_dict))
            else:
                    print_help()
        elif sys.argv[1] == '--intent':
            print(intent(sys.argv[2]))
        elif sys.argv[1] == '--recommendation':
            print(recommendation(sys.argv[2]))
        else:
            print_help()
    else:
        print_help()

