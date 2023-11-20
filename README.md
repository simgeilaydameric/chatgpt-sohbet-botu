# ChatGPT Sohbet Botu

Bu Python kodu, PyQt5 kullanılarak basit bir GUI (Grafiksel Kullanıcı Arayüzü) içeren bir sohbet uygulamasını oluşturan bir programdır. Bu uygulama, OpenAI tarafından sağlanan GPT-3.5-turbo modelini kullanarak metin tabanlı sohbet yapma yeteneğine sahiptir.

![ChatGPT-ile-Baglanti](https://github.com/simgeilaydameric/ChatGPT-ile-Baglanti/blob/main/chatbot.png)

## Kullanım

1. Projeyi bilgisayarınıza klonlayın.
2. OpenAI'den alınan API anahtarınızı `openai.api_key` değişkenine ekleyin.
3. Uygulamayı çalıştırın.

## İşlevsellik

- Birincil pencere ve içeriği oluşturulur.
- Kullanıcının metin girişi için bir QTextEdit kutusu eklenir.
- ChatGPT'nin cevaplarını görüntülemek için başka bir QTextEdit kutusu eklenir.
- "Sohbet Et" adlı bir düğme eklenir ve bu düğmeye tıklandığında `chatWithGPT` fonksiyonu çağrılır.
- `chatWithGPT` fonksiyonu, kullanıcının girdisini alır, GPT-3.5-turbo modeliyle iletişim kurar ve modelin cevabını ikinci QTextEdit kutusuna ekler.
- OpenAI'nin Python kütüphanesi olan `openai` kullanılarak GPT-3.5-turbo modeliyle iletişim sağlanır.

## API Anahtarı Alma

API anahtarınızı almak için izleyebilirsiniz: [API-Key-Video](https://www.youtube.com/watch?v=aVog4J6nIAU) 


## Önemli Notlar

- Projeyi çalıştırmadan önce OpenAI'den edinilen API anahtarını eklemeyi unutmayın.
- OpenAI API'sini kullanabilmek için gerekli kütüphanenin (`openai`) yüklü olduğundan emin olun.
- Bu uygulama, basit bir sohbet arayüzü sağlar ve kullanıcının girişine yanıt olarak GPT-3.5-turbo modelinden gelen cevapları görüntüler.

## Katkılar

Bu proje açık kaynaklıdır. Katkıda bulunmak isterseniz, lütfen forklayın ve pull request gönderin.
