{
    "targets": [
        {
            "target_name": "hello",
            'include_dirs': [
                "<!(node -p \"require('node-addon-api').include_dir\")",
                # "/Users/plum/Desktop/addon/lib/Plum2.framework"
                # "lib/Plum2.framework -F./lib"

            ],
            # 'cflags!': ['-fno-exceptions'],
            # 'cflags_cc!': ['-fno-exceptions'],
            # "libraries": [
            #     '-F/Users/plum/Desktop/addon/lib/ -framework Plum2',
            # "-Wl, /Users/plum/Desktop/addon/lib/Plum2.framework/Plum2"
            # ],
            'conditions': [
                ["OS=='mac'", {
                    "sources": [
                        "src/hello_mac.mm"
                    ],
                    'include_dirs': [
                        "<!(pwd)/lib/Plum1.framework -F/Users/plum/Desktop/addon/lib/ "
                    ],
                    'defines': ['NAPI_DISABLE_CPP_EXCEPTIONS'],
                    'link_settings': {
                        'libraries': [
                            '-Wl,-rpath,<!(pwd)/lib',
                            '-F<!(pwd)/lib -framework Plum1',
                        ],
                    },
                    'xcode_settings': {
                        'OTHER_CFLAGS': [
                            '-ObjC++'
                        ]
                    }

                }, ],
                ["OS=='win'", {
                    "sources": [
                        "src/hello_win.cc"
                    ],
                    'include_dirs': [
                        # "<!(pwd)/lib/Plum1.framework -F/Users/plum/Desktop/addon/lib/ "
                        "lib\win\include"
                    ],
                    'defines': ['NAPI_DISABLE_CPP_EXCEPTIONS'],
                    'link_settings': {
                        'libraries': [
                            '-Wl,-rpath,lib\win',
                            # '-F<!(pwd)/lib -framework Plum2',
                            "../lib/win/Hello.lib",

                        ],
                    },

                    # "xcode_settings": {
                    #     "cflags_cc": [
                    #         "-F/Users/plum/Desktop/addon/lib/ -framework Plum2"
                    #     ],
                    # }
                    # "copies":
                    # [
                    #     {
                    #         'destination': 'build/Debug',
                    #         'files': [
                    #             'lib/win/Hello.dll'
                    #         ]
                    #     }
                    # ]

                }, ],
            ],
        }
    ],
}
