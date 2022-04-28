import yaml
def readYaml(fileName):
    file = open(fileName,'r',encoding='utf-8')
    data = yaml.load(file)
    print(data)
    return data