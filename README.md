<div align="center">

  # 📖 mangal-to-calibre

  <sub>Just a simple script I use to download manga from [mangal](https://github.com/metafates/mangal) and automatically import it into [calibre](https://github.com/kovidgoyal/calibre) correctly.</sub>

</div>

> [!NOTE]
> Personalized script for really only my usage, so I prefer you don't use it or contribute to it.

# 🛠️ Installation
```sh
git clone https://github.com/THEGOLDENPRO/mangal-to-calibre
cd mangal-to-calibre
make
make install
```

# 🖥️ Usage
```sh
manga "Oshi No Ko" -c 0-2
```
> Should download and add the manga oshi no ko chapter 1 to 3 to your calibre library.
> Anything passed to `-c` or `--chapters` get's passed directly to mangal.
> If you don't like the binary name change it yourself. :)
