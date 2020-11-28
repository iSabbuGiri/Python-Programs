def tags(tag, string):
    return "<%s><%s></%s>" %(tag, string, tag)
print(tags('h1','Insight Workshop'))    