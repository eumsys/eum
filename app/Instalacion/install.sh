#!/bin/bash
progress_bar()
{
  local PROG_BAR_MAX=${1:-30}
  local PROG_BAR_DELAY=${2:-1}
  local PROG_BAR_TODO=${3:-"."}
  local PROG_BAR_DONE=${4:-"#"}
  local i

  echo -en "["
  for i in `seq 1 $PROG_BAR_MAX`
  do
    echo -en "$PROG_BAR_TODO"
  done
  # Note: The following line echoes:
  # 1)   "]" (to end the "[...]" bar)
  # 2)   Control-M (aka Carriage Return) (aka Octal \0015)
  # 3)   "[" (to replace the original "[" and put the cursor in the right place)
  #echo -en "]^M["
  echo -en "]\0015["
  for i in `seq 1 $PROG_BAR_MAX`
  do
    echo -en "$PROG_BAR_DONE"
    sleep .05
  done
  echo
}



# Verificando archivo .bashrc
if [ -e ~/.bashrc ];
    echo "Configurando arranque..."
    progress_bar 20
    then
        sudo chmod 777 ~/.bashrc
    else
        touch ~/.bashrc 
        sudo chmod 777 ~/.bashrc
fi


# Verificando archivo de configuracion
echo "Cargando configuracion por Default...(1)"
progress_bar 20


if [ -e /opt/app/config/config.ini ];
    then
        echo "config.ini ya existe"
        #cat ~/Documents/eum/app/Config/config.ini
        #chmod 777 ~/.bashrc
    else
        if [ -d /opt/app/config/ ];
            then
                mv ~/Documents/eum/app/Config/config.ini /opt/app/config/
            else
                sudo mkdir -p /opt/app/config
                sudo mv ~/Documents/eum/app/Config/config.ini /opt/app/config/
        fi
fi

# Actualizando repositorio

cd ~/Documents/eum
echo "Descargando actualizaciones..."
progress_bar 20
git status

# Instalando requeriments.txt
#cd ~/Documents/eum/
if [ -e ~/Documents/eum/requirements.txt ];
    then
        echo "Instalando librerias..."
        progress_bar 20
        pip3 install -r ~/Documents/eum/requirements.txt
        sudo apt-get install xdotool
    else
        echo "No,no existe"
        touch ~/.bashrc 
fi
# Actualizando BD
echo "Actualizando BD..."
progress_bar 20
cd ~/Documents/eum/app/cajeroW/BD
sudo PGPASSWORD='Postgres3UMsd6' -u postgres psql -f build.sql
