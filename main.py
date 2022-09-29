def define_env(env):
    env.variables['test'] = True

def on_post_page_macros(env):
    """
    Actions to be done after macro interpretation,
    when the markdown is already generated
    """
    if env.variables['test'] == True:
        env.raw_markdown = env.raw_markdown.replace('%I%', '???+ tip "internal informations"')
        # env.raw_markdown = env.raw_markdown.replace('C%', '    ')
        env.raw_markdown = env.raw_markdown.replace('%R%', '???+ quote "customereply"')
        env.raw_markdown = env.raw_markdown.replace('%M%', '    === "macro"')
        # env.raw_markdown = env.raw_markdown.replace('CD%', '        ')
        
        env.raw_markdown = env.raw_markdown.replace('%A%', '    === "answer"')
