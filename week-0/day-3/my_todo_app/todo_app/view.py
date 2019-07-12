def todo_view(todos):
    the_view = 'List of my todos:' + '<br/>'
    for todo in todos:
        the_view += ( todo + '<br/>' )

    the_view += '---- LIST ENDS HERE ---'
    return the_view