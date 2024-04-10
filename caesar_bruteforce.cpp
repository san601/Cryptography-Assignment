#include <bits/stdc++.h>
using namespace std;

void caesar_decrypt_bruteforce(string cipher_text){
    int length = cipher_text.length();
    for (int shift = 1; shift < 26; ++shift){
        string cp = cipher_text;    // I dont want to learn competitive programming anymore
        for (int i = 0; i < length; ++i){
            if (!isalpha(cp[i])){
                continue;
            }
            else {
                if ('a' <= cp[i] && cp[i] <= 'z'){
                    cp[i] = (cp[i] - 'a' + shift) % 26 + 'a';
                }
                else {
                    cp[i] = (cp[i] - 'A' + shift) % 26 + 'A';
                }
            }
        }
        cout << "[o] Result for shift amount = " << shift << ": " << cp << '\n';
    }
}

int main(){
    cout << "[o] Enter cipher text to decrypt: ";
    string cipher_text; getline(cin, cipher_text);
    caesar_decrypt_bruteforce(cipher_text);
}