import yaml
def params():#从yaml读取参数后，转换格式
    with open('testcase.yaml', 'r') as f:
        y = yaml.unsafe_load(f)
    l = []
    for i in y.values():
        l.append(tuple(i.values()))
    return l