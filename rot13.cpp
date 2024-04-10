#include <bits/stdc++.h>
using namespace std;

string rot13(string plain){
    for (int i = 0; i < plain.length(); ++i){
        if (!isalpha(plain[i])) continue;
        else {
            if ('A' <= plain[i] && plain[i] <= 'Z'){
                plain[i] = (plain[i] - 'A' + 13) % 26 + 'A';
            }
            else {
                plain[i] = (plain[i] - 'a' + 13) % 26 + 'a';
            }
        }
    }
    return plain;
}

string decrypt(string cipher){
    for (int i = 0; i < cipher.length(); ++i){
        if (!isalpha(cipher[i])) continue;
        else {
            if ('A' <= cipher[i] && cipher[i] <= 'Z'){
                cipher[i] = (cipher[i] - 'A' + 13) % 26 + 'A';
            }
            else {
                cipher[i] = (cipher[i] - 'a' + 13) % 26 + 'a';
            }
        }
    }
    return cipher;
}

int main(){
    cout << "[o] Choice: \n1. Encrypt\n2. Decrypt\n>>> ";
    int choice; cin >> choice;
    if (choice == 1) {
        cout << "[o] Enter text to encrypt: ";
        string plain; cin >> plain;
        cout << "[o] Encrypted: " << rot13(plain);
    } 
    else if (choice == 2){
        cout << "[o] Enter text to decrypt: ";
        string cipher; cin >> cipher;
        cout << "[o] Decrypted: " << decrypt(cipher);
    }
    else cout << "Invalid choice!";
    
}