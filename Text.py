from string import Template

def generatorText(keywords='rabbit',type='advantage'):
    prompt = Template("""Please, as a teacher who tells stories to 5-year-old children, use the following content to generate a fairy tale: 1 Keywords: ${keywords}, 2 Subject: ${type},
    If you encounter content that cannot be generated, please ignore it.Considering children's age group, educational significance, safety and other factors, at the same time adopting vivid and interesting characters and plots.The story is for five-year-olds that require simple vocabulary.do not repeat these sentences.""")
    text=prompt.substitute(keywords=keywords,type=type)
    return text