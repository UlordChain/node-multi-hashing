// Copyright (c) 2012-2013 The Cryptonote developers
// Distributed under the MIT/X11 software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.
#include "hash.h"

void cryptonight_hash(const char* input, char* output, int len)
{
    cn_slow_hash(input, len, output);
}
void cryptonight_fast_hash(const char* input, char* output, int len)
{
    cn_fast_hash(input, len, output );
}

