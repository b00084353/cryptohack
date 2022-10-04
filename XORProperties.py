from Crypto.Util.number import *

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
KEY2X1 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KEY2X3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
FLAGX1X2X3 = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"


key1int = int(KEY1,16)
key2X1int = int(KEY2X1,16)
key2X3int = int(KEY2X3,16)
key4int = int(FLAGX1X2X3,16)


key2int = (key1int ^ key2X1int)
key3int = (key2int ^ key2X3int)



key1bytes=(bytes.fromhex(KEY1))
key2x1bytes=(bytes.fromhex(KEY2X1))
plainflag = (key1int ^ key2int ^ key3int ^ key4int)
print(plainflag)
print (long_to_bytes(plainflag))
