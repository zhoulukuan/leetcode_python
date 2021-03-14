class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        na, nb, ds, dg = 0, 0, {}, {}
        for i in range(n):
            if secret[i] == guess[i]:
                na += 1
            else:
                if secret[i] in ds: 
                    ds[secret[i]] += 1
                else:
                    ds[secret[i]] = 1
                if guess[i] in dg:
                    dg[guess[i]] += 1
                else:
                    dg[guess[i]] = 1
        
        for key, value in ds.items():
            if key in dg:
                nb += min(value, dg[key])
        
        return str(na) + 'A' + str(nb) + 'B'
