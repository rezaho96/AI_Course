import jmespath

people={
    "People":
        [
            {"id":21,"name":"ali","age":25,"children":[{"name":"mina","age":5}]},
            {"id":21,"name":"mohamad","age":35,"children":[{"name":"nazgol","age":4},{"name":"mahi","age":2}]},
            {"id":21,"name":"saber","age":20,"children":[]}
        ]
}

# print(jmespath.search("People[*]",people))
# print(jmespath.search("People[*].name",people))
# print(jmespath.search("People[1].name",people))
# print(jmespath.search("People[1].children[*].name",people))
# print(jmespath.search("People[:2].children[*].name",people))
# print(jmespath.search("People[*].children[2].name",people))


print(jmespath.search("People[?age==`25`].[name,age,id]",people)[0])
print(jmespath.search("People[?age>`30`].children[*].name",people))