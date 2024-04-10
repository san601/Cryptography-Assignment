#include <bits/stdc++.h>
using namespace std;

string caesar_encrypt(string plain_text, int shift){
    int length = plain_text.length();
    for (int i = 0; i < length; ++i){
        if (isalpha(plain_text[i])){
            if (plain_text[i] >= 'a' && plain_text[i] <= 'z'){
                plain_text[i] = (plain_text[i] - 'a' + shift) % 26 + 'a';
            }
            else {
                plain_text[i] = (plain_text[i] - 'A' + shift) % 26 + 'A';
            }
        }
        else continue;
    }
    return plain_text;
}

int main(){
    string plain_text; 
    cout << "[o] Input plain text to encrypt: ";
    getline(cin, plain_text);

    cout << "[o] Shift amount: ";
    int shift; cin >> shift;
    if (shift < 0){
        cout << "[x] Cannot shift with negative values!\n";
        return 0;
    }

    string cipher_text = caesar_encrypt(plain_text, shift);
    cout << ">> Encrypted text: " << cipher_text;
}