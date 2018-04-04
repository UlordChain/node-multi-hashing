{
    "targets": [
        {
            "target_name": "multihashing",
            "sources": [
                "multihashing.cc",
                "aesb.c",
                "chacha8.c",
                "crypto-ops-data.c",
                "hash.c",
                "hash-extra-groestl.c",
                "hash-extra-skein.c",
                "keccak.c",
                "random.c",
                "slow-hash.c",
                "blake256.c",
                "crypto-ops.c",
                "groestl.c",
                "hash-extra-blake.c",
                "hash-extra-jh.c",
                "jh.c",
                "oaes_lib.c",
                "skein.c",
                "tree-hash.c",
                "cryptonight.c"
            ],
            "include_dirs": [
                "crypto",
                "<!(node -e \"require('nan')\")",
            ],
            "cflags": [
                "-D_GNU_SOURCE -maes -fPIC -Ofast -flto -fuse-linker-plugin -funroll-loops -funswitch-loops -fpeel-loops"
            ],
            "cflags!": [ 
                "-O2", "-fno-strict-aliasing", "-fno-tree-vrp", "-fno-omit-frame-pointer"
            ],
            "ldflags": [
                "-fPIC -Ofast -flto -fuse-linker-plugin"
            ],
            "cflags_cc": [
                "-std=c++0x -maes -march=native"
            ]
        }
    ]
}
