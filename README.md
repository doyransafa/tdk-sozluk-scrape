### tdk-sozluk-scrape
# En fazla anlama sahip Türkçe kelimeler

Öncelikle bu çalışma dilbilimsel ya da sözük/kelime bilimine dair herhangi bir iddia içermemektedir. Yalnızca basit bir web scraping ve SQL projesidir.

Çalışmanın ana fikri ünlü YouTube kanalı Vsauce'un ["The Word With The Most Definitions."](https://www.youtube.com/watch?v=SRKXSzbGUm4) videosundan esinlenmiştir. Videoda bahsedildiği üzere İngilizce sözlükte "set" kelimesinin 400, "run" kelimesinin 600'den fazla anlamı bulunmaktadır.

Türkçe sözlükteki tüm keliemelerin listelendiği dijital bir kaynak bulamadığım için internetten ulaşabildiğim en büyük kelime seti [(Vikisözlük)](https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:Anasayfa) üzerinden topladığım kelimeleri bir Python scripti yardımıyla TDK online sözlükte (https://sozluk.gov.tr/) arattım. 63 binden fazla kelime araması tamamlandıktan sonra aradığım cevaba ulaştım.

Peki en fazla anlama sahip Türkçe kelime hangisi? TDK online sözlüğe göre ["çıkmak"](https://sozluk.gov.tr/?/%C3%A7%C4%B1kmak), 56 anlamla en fazla anlama sahip kelime. Çıkmak kelimesini 47 anlamla ["tutmak"](https://sozluk.gov.tr/?/tutmak) ve 43 anlamla ["çekmek"](https://sozluk.gov.tr/?/%C3%A7ekmek) kelimeleri takip ediyor. En fazla sayıda anlama sahip ilk 20 kelime aşağıdaki şekilde:

<img width="216" alt="Screenshot 2023-07-12 at 15 48 44" src="https://github.com/doyransafa/tdk-scrape/assets/72417108/35fa1732-35f1-4f95-965a-821a1796b27b">

Beklenildiği üzere kelimelerin tamamı fiil. Fiil olmayan kelimeler arasında en fazla anlama sahip 3 kelime ise 19 anlamla "iş", 18 anlamla "ağırlık" ve 17 anlamla "ağır".

Peki, elimizdeki bu 63 bin kelime aramasından başka nelere ulaşabiliriz? https://sozluk.gov.tr/ kelime anlamlarına ek olarak kelime kökenleri ve ünlü Türk yazarların metinlerinden kelimelere dair örnek cümleler içeriyor. Veriyi SQL ve Python'da biraz temizledikten sonra en fazla hangi yabancı dillerden kelime alındığına ve en fazla sayıda referans gösterilen yazarlara ulaşabiliyoruz.

## En fazla sayıda kelimeye sahip yabancı diller:

<img width="168" alt="Screenshot 2023-07-12 at 15 50 28" src="https://github.com/doyransafa/tdk-scrape/assets/72417108/99e5f22b-af9a-4c7b-ba24-9c4556038146">￼

Arapça, Fransızca ve Farsça ilk 3 sırada yer alıyor. Not: 400 adet kelime Arapça ve Farsça kelimelerin birleşiminden elde edilmiştir. Bu tarz kelimeler her iki dil için de sayılmıştır.

## En fazla sayıda referans gösterilen yazarlar:

63 bin kelime içerisinde toplam 229 yazardan cümle örneğine yer verilmiştir. En fazla referans gösterilen 20 yazar aşağıdaki şekildedir:

<img width="181" alt="Screenshot 2023-07-12 at 15 51 10" src="https://github.com/doyransafa/tdk-scrape/assets/72417108/98d2c6d3-d537-4cca-955a-4a2ce3457980">
