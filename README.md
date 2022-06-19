# Witaj w ApiusLAB  
![apiuslab](https://marekplaza.github.io/apiuslab/apiuslab.png)

ApiusLAB to aplikacja do przyjaznego wykonywania szkoleń i prezentacji technologii sieciowych Arista Networks w oparciu o skontenryzowany obraz systemu operacyjengo EOS (cEOS) oraz narzędzie containerlab [containerlab.dev](https://containerlab.dev). 
Przygotowaliśmy dla Ciebie kilka ciekawych LABów bazujących na rozwiązaniach Arista Networks, m.in. z zakresu: MLAG, L&S, EVPN i telemetria. Życzymy udanej przygody z kontenerami i technologiami sieciowymi.

### Jak korzystać?

Aplikacja występuje w postacji kontenera do pobrania z oficjalnego publicznego Docker Hub'a:

```bash
    sudo docker pull marekplaza/apiuslab:2022SSH2

```

klonujemy repozytorium `git clone https://github.com/marekplaza/apiuslab.git`, przechodzimy do katalogu `cd apiuslab/` i uruchamiamy poleceniem:

```bash
    sudo docker run --rm -it --privileged \
 --network host \
 -v /var/run/docker.sock:/var/run/docker.sock \
 -v /var/run/netns:/var/run/netns \
 -v /etc/hosts:/etc/hosts 
 --pid="host" \
 -v $(pwd):$(pwd) \
 -w $(pwd)  \
 marekplaza/apiuslab:2022SSH2

```

W wyniku czego powinniśmy otrzymać konsolę ułatwiającą nasze labowanie:

```bash
                                                                                                              
          ..         ...                                                                                  
        :!77!.      ~77!^                                                                                 
      .~7777~       :!777!:                                                                               
     :!777!:  ^!!~.  .~7777^                                                                              
   .~7777^  .!777~. .. :!777!:                                   .^~:                                     
  .7?777:  :7777^ .!77~ .!777?^                                  5&&#7                                    
  .~777!~. .~777~. ^!~: ^!777!.                                  !5PY^                                    
    :!7!7!:  :!77!.   .~7!!!^    .^!777~:.~^~:  :~~^.:~777!:     .^^^  .^~~:     .^~~:   .^!777~^         
      ^!!!7~. .^^:   ^!!!7~.   .JG#&###&#G##&?  5###G#&##&&#P7   ?&##^ :###Y     :###Y  ?G##BB#&#G7       
       .~777!.      ~777!:    :G##G7^:^!5####?  5###BJ~::~JB##5. ?###^ :###Y     :###Y !&##J...7P5Y^      
         ^~~^       :~~^.     5&#B:      ?###?  5###~      ~##&? ?###^ :###Y     :B##Y :G###G5Y?7^        
                              5##G.      7###?  5###^      ^##&? ?###^ :###Y     ~###Y   ~?YPGB###G^      
                              ~###5~...:?B###?  5###G!:..:!G##G: ?###^ .B##B7:.:!G###Y ~?JJ^  .7##&Y      
                               ^5#&&BBB#&###&?  5####&#BB#&&BY:  ?&##^  ~G#&&#B#&B##&Y !B&&#GPPB##P:      
                                 :7JYYJ?~^777^  5##B~!?YYY?!:    ^777.   .~?JYY?!:777~  .~7JYYYJ7^        
                                                5##B:                                                     
                                                5&#B:                        T E C H N O L O G I E S      
                                                ?P55.                                                     
                                                                                                        

  Status LAB'a: 
+---+-------------------------------------------+-----------+----------+--------------+---------------------------------+------+---------+-------------------+--------------+
| # |                 Topo Path                 | Lab Name  |   Name   | Container ID |              Image              | Kind |  State  |   IPv4 Address    | IPv6 Address |
+---+-------------------------------------------+-----------+----------+--------------+---------------------------------+------+---------+-------------------+--------------+
| 1 | ../test/apiuslab/LAB1_MLAG/LAB1_MLAG.yaml | LAB1_MLAG | CLIENT-1 | 1832039eabec | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.1/24  | N/A          |
| 2 |                                           |           | CLIENT-2 | 034fa3b9b8b0 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.2/24  | N/A          |
| 3 |                                           |           | LEAF-1   | f8e12dbcd101 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.12/24 | N/A          |
| 4 |                                           |           | LEAF-2   | f125f9195ef5 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.13/24 | N/A          |
| 5 |                                           |           | LEAF-3   | bd17d7473194 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.14/24 | N/A          |
| 6 |                                           |           | LEAF-4   | 7de176deb149 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.15/24 | N/A          |
| 7 |                                           |           | SPINE-1  | 7cc0f23c2897 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.10/24 | N/A          |
| 8 |                                           |           | SPINE-2  | 63077f4f0964 | marekplaza/ceos64-lab:4.27.1.1F | ceos | running | 172.100.100.11/24 | N/A          |
+---+-------------------------------------------+-----------+----------+--------------+---------------------------------+------+---------+-------------------+--------------+

========== Menu Głowne: Opcje wyboru ==========

  Wybierz LAB'a:

     01. MLAG
     02. Leaf & Spine
     03. VxLAN
     04. EVPN VxLAN L2
     05. EVPN VxLAN L3
     06. Telemetria gRPC

     88. Reset
     99. Wyjście

 Co chciałbyś zrobić? 
```

### Więcej informacji:
Arista Networks [arista.com](https://arista.com) <br/>
Apius Technologies [apius.pl](https://apius.pl)   

🐳 + 🧪 (c) 2022 Marek Plaza ;)

