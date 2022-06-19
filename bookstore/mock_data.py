import random

DESCRIPTION_DATA = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum vulputate rhoncus commodo. Aliquam quis consectetur augue, in vulputate felis. Donec sodales posuere fermentum. Suspendisse dignissim ligula quis aliquet dapibus. Duis lacus erat, consequat eu fringilla eu, commodo et justo. Nulla et turpis eu nibh maximus tincidunt tristique sit amet nisl. Praesent felis quam, porttitor interdum dolor vel, consectetur convallis tortor. Nullam imperdiet ut tortor sed mattis. Cras venenatis blandit massa at ultricies.Aliquam eget finibus urna. In auctor hendrerit purus, vitae sollicitudin erat semper non. Phasellus placerat euismod nulla, nec tempus arcu porta ut. Integer nisi metus, vestibulum in tempor a, viverra in tortor. Proin vitae augue nulla. Sed posuere gravida rhoncus. Donec suscipit mattis dignissim. Cras elementum maximus faucibus. Sed fringilla turpis a ex sagittis, ut ultrices nisi molestie. Pellentesque tincidunt ipsum diam, non volutpat urna cursus efficitur. Phasellus bibendum, nulla eu ornare cursus, lectus tellus iaculis lacus, sed egestas tellus odio non risus.In commodo id velit non consequat. Integer lacinia massa at dolor hendrerit cursus. Fusce dui sem, commodo id mauris ac, convallis condimentum orci. In mattis risus in est ullamcorper aliquam. In id pulvinar dolor, et congue turpis. Fusce quam velit, facilisis eu aliquet nec, pretium ut erat. Quisque vitae quam posuere, eleifend dolor id, porttitor risus. Nullam quis elit ut dolor lobortis imperdiet sit amet eu sapien. Duis aliquet finibus dolor, sit amet laoreet lectus pharetra nec. Cras tellus tellus, auctor a urna non, dignissim vulputate neque. Ut purus ex, ultrices non aliquam ac, volutpat id ante. Sed a ultrices purus.Pellentesque et lectus elit. Vivamus feugiat, nulla sed dignissim scelerisque, ante leo ultricies dui, eget rhoncus massa elit nec nibh. Curabitur consectetur tortor leo, id auctor ligula sollicitudin sed. Ut id commodo eros. In scelerisque tincidunt malesuada. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Nulla non gravida tellus, quis tristique eros. Maecenas molestie, augue a pellentesque euismod, libero velit efficitur ex, non finibus magna diam quis ante. Nam vulputate hendrerit sem, id tempor nibh dapibus in. Sed vitae felis erat. Aliquam sit amet congue quam. Cras vitae nibh maximus, porta quam a, sollicitudin enim.Praesent consequat quis nunc in faucibus. Sed arcu eros, ullamcorper id ante ac, pretium rutrum lacus. Nullam ullamcorper ex quis sapien cursus, nec eleifend leo dignissim. Quisque tempus erat nec ligula scelerisque, ac imperdiet eros maximus. Cras iaculis lectus vitae leo viverra rutrum. Aenean viverra ex ac dui rutrum fermentum. Suspendisse vestibulum eget orci sed molestie. Integer ultricies erat accumsan est dictum, ac convallis augue facilisis. Donec volutpat sit amet velit in dignissim. Donec ornare lectus quis metus sodales interdum. Donec metus nulla, rhoncus id vehicula eu, vulputate at erat. Nullam tortor sapien, rutrum in elit nec, accumsan volutpat ipsum. In hac habitasse platea dictumst. Cras iaculis porttitor mauris, vitae commodo dui hendrerit in.'

BOOKS = [{
    'id': i,
    'author_id': i,
    'title': f'Book {i}',
    'released_year': random.randint(1990, 2022),
    'description': DESCRIPTION_DATA[
                   random.randint(
                       0,
                       len(DESCRIPTION_DATA) // 2 - 1
                    )
                   :
                   random.randint(
                       len(DESCRIPTION_DATA) // 2 + 1,
                       len(DESCRIPTION_DATA)
                    )
                   ]

} for i in range(1, 11)]

AUTHORS = [{
    'id': i,
    'first_name': f'Name {i}',
    'last_name': f'Last name {i}',
    'age': random.randint(18, 100),
} for i in range(1, 11)]
