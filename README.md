### tdk-sozluk-scrape
# En fazla anlama sahip Türkçe kelimeler

Öncelikle bu çalışma dilbilimsel ya da sözük/kelime bilimine dair herhangi bir iddia içermemektedir. Yalnızca basit bir web scraping ve SQL projesidir.

Çalışmanın ana fikri ünlü YouTube kanalı Vsauce'un ["The Word With The Most Definitions."](https://www.youtube.com/watch?v=SRKXSzbGUm4) videosundan esinlenmiştir. Videoda bahsedildiği üzere İngilizce sözlükte "set" kelimesinin 400, "run" kelimesinin 600'den fazla anlamı bulunmaktadır.

Türkçe sözlükteki tüm keliemelerin listelendiği dijital bir kaynak bulamadığım için internetten ulaşabildiğim en büyük kelime seti [(Vikisözlük)](https://tr.wiktionary.org/wiki/Vikis%C3%B6zl%C3%BCk:Anasayfa) üzerinden topladığım kelimeleri bir Python scripti yardımıyla TDK online sözlükte (https://sozluk.gov.tr/) arattım. 63 binden fazla kelime araması tamamlandıktan sonra aradığım cevaba ulaştım.

Peki en fazla anlama sahip Türkçe kelime hangisi? TDK online sözlüğe göre ["çıkmak"](https://sozluk.gov.tr/?/%C3%A7%C4%B1kmak), 56 anlamla en fazla anlama sahip kelime. Çıkmak kelimesini 47 anlamla ["tutmak"](https://sozluk.gov.tr/?/tutmak) ve 43 anlamla ["çekmek"](https://sozluk.gov.tr/?/%C3%A7ekmek) kelimeleri takip ediyor. En fazla sayıda anlama sahip ilk 20 kelime aşağıdaki şekilde:

<img width="219" alt="Pasted Graphic 1" src="https://github.com/doyransafa/tdk-sozluk-scrape/assets/72417108/8b1784c2-d950-427b-b587-ab8a8554973e">


Beklenildiği üzere kelimelerin tamamı fiil. Fiil olmayan kelimeler arasında en fazla anlama sahip 3 kelime ise 19 anlamla "iş", 18 anlamla "ağırlık" ve 17 anlamla "ağır".

Peki, elimizdeki bu 63 bin kelime aramasından başka nelere ulaşabiliriz? https://sozluk.gov.tr/ kelime anlamlarına ek olarak kelime kökenleri ve ünlü Türk yazarların metinlerinden kelimelere dair örnek cümleler içeriyor. Veriyi SQL ve Python'da biraz temizledikten sonra en fazla hangi yabancı dillerden kelime alındığına ve en fazla sayıda referans gösterilen yazarlara ulaşabiliyoruz.

## En fazla sayıda kelimeye sahip yabancı diller:

<img width="172" alt="Pasted Graphic 2" src="https://github.com/doyransafa/tdk-sozluk-scrape/assets/72417108/52ca65c2-5028-4903-82ac-5b6088eb86f3">

Arapça, Fransızca ve Farsça ilk 3 sırada yer alıyor. Not: 400 adet kelime Arapça ve Farsça kelimelerin birleşiminden elde edilmiştir. Bu tarz kelimeler her iki dil için de sayılmıştır.

## En fazla sayıda referans gösterilen yazarlar:

63 bin kelime içerisinde toplam 229 yazardan cümle örneğine yer verilmiştir. En fazla referans gösterilen 20 yazar aşağıdaki şekildedir:

<img width="185" alt="Pasted Graphic 3" src="https://github.com/doyransafa/tdk-sozluk-scrape/assets/72417108/6aba22d2-e008-4deb-9962-50d74954cd35">
