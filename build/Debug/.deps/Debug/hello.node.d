cmd_Debug/hello.node := c++ -bundle -undefined dynamic_lookup -Wl,-no_pie -Wl,-search_paths_first -mmacosx-version-min=10.13 -arch x86_64 -L./Debug -stdlib=libc++  -o Debug/hello.node Debug/obj.target/hello/src/hello.o -Wl,-rpath,/Users/plum/Desktop/addon/lib -F/Users/plum/Desktop/addon/lib -framework Plum2