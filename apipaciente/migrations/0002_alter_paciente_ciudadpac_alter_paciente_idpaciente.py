# Generated by Django 4.1.7 on 2023-05-26 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apipaciente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='ciudadPac',
            field=models.CharField(choices=[['BogotÃ¡', 'MedellÃ\xadn'], ['Cali', 'Barranquilla'], ['Cartagena', 'CÃºcuta'], ['Bucaramanga', 'Pereira'], ['Santa Marta', 'IbaguÃ©'], ['Villavicencio', 'Valledupar'], ['Manizales', 'Pasto'], ['Armenia', 'MonterÃ\xada'], ['Neiva', 'PopayÃ¡n'], ['Sincelejo', 'Riohacha'], ['Tunja', 'QuibdÃ³'], ['Florencia', 'Yopal'], ['Mocoa', 'San AndrÃ©s'], ['Arauca', 'Puerto carreÃ±o'], ['MitÃº', 'Florencia'], ['Tumaco', 'Turbo'], ['Puerto AsÃ\xads', 'Girardot'], ['Maicao', 'Pamplona'], ['Yumbo', 'ChÃ\xada'], ['JamundÃ\xad', 'Buga'], ['TuluÃ¡', 'Envigado'], ['Rionegro', 'Soacha'], ['ZipaquirÃ¡', 'Ipiales'], ['Caucasia', 'Lorica'], ['La Dorada', 'Pitalito'], ['ChigorodÃ³', 'SonsÃ³n'], ['ChiquinquirÃ¡', 'El Carmen de Viboral'], ['La Ceja', 'San JosÃ© del Guaviare'], ['Sogamoso', 'Duitama'], ['FusagasugÃ¡', 'Dosquebradas'], ['Villa del Rosario', 'AcacÃ\xadas'], ['Yarumal', 'Sabanalarga'], ['Soledad', 'Barrancabermeja'], ['GarzÃ³n', 'CiÃ©naga'], ['Puerto BerrÃ\xado', 'El Cerrito'], ['Piedecuesta', 'Palmira'], ['Barrancas', 'CiÃ©naga de Oro'], ['La UniÃ³n', 'Mosquera'], ['San Carlos', 'Candelaria'], ['San Juan Nepomuceno', 'Cotorra'], ['Pitalito', 'San Luis'], ['San SebastiÃ¡n de Mariquita', 'La Plata'], ['La Jagua de Ibirico', 'Valle del Guamuez'], ['La Tebaida', 'San Marcos'], ['Ayapel', 'CurumanÃ\xad'], ['San Onofre', 'Tibasosa'], ['Cumaral', 'San Jacinto'], ['El Banco', 'San JosÃ© de UrÃ©'], ['Quimbaya', 'Granada'], ['Samaniego', 'San Roque'], ['Chaparral', 'La Virginia'], ['La Virginia', 'Talaigua Nuevo'], ['San JosÃ© del Palmar', 'AnzoÃ¡tegui'], ['Puerto Rico', 'TuchÃ\xadn'], ['La Apartada', 'Silvia'], ['La Cruz', 'Candelaria'], ['Ricaurte', 'San Juan del Cesar'], ['Salamina', 'Almaguer'], ['Turbana', 'SupÃ\xada'], ['San Vicente del CaguÃ¡n', 'La Cumbre'], ['San Juan Nepomuceno', 'NechÃ\xad'], ['TadÃ³', 'TÃ³paga'], ['Pacho', 'San AndrÃ©s de Tumaco'], ['SaboyÃ¡', 'Venadillo'], ['San Juanito', 'Sabana de Torres'], ['TimbÃ\xado', 'Salamina'], ['LÃ\xadbano', 'Santa BÃ¡rbara de Pinto'], ['SibatÃ©', 'Barrancas'], ['Malambo', 'San Luis de Gaceno'], ['PuracÃ©', 'AlbÃ¡n'], ['La Paz', 'TarazÃ¡'], ['San Roque', 'Campo de la Cruz'], ['Zarzal', 'La Plata'], ['San Cayetano', 'San Pedro de UrabÃ¡'], ['La Loma', 'San JosÃ© de Miranda'], ['CiÃ©naga de Oro', 'San MartÃ\xadn'], ['Suaita', 'Santana'], ['San Diego', 'Guayabal de SÃ\xadquima'], ['Puerto Escondido', 'El Cerrito'], ['Planadas', 'Tunja'], ['San Francisco', 'Corinto'], ['Algeciras', 'La Victoria'], ['San Juan Nepomuceno', 'El Paujil'], ['Salamina', 'San AndrÃ©s de CuerquÃ\xada'], ['Samaniego', 'TolÃº'], ['La Jagua del Pilar', 'San Juan de Arama'], ['Valdivia', 'San JosÃ© del Palmar'], ['Valdivia', 'San JosÃ© del Palmar'], ['San Juan de Rioseco', 'La Vega'], ['Yacuanquer', 'San Luis'], ['Ansermanuevo', 'El TablÃ³n de GÃ³mez'], ['Lebrija', 'PÃ¡ez'], ['Luruaco', 'SonsÃ³n'], ['TÃ¡mesis', 'Buenavista'], ['San SebastiÃ¡n', 'Guachucal'], ['Piamonte', 'San Vicente del CaguÃ¡n'], ['Marmato', 'San JosÃ© de Miranda'], ['PurÃ\xadsima', 'La Belleza'], ['Santuario', 'Gambita'], ['San Pablo de Borbur', 'San Carlos'], ['Cantagallo', 'Tello'], ['Oporapa', 'Silvia'], ['Santa Rosa de Cabal', 'La Apartada y La Frontera'], ['ValparaÃ\xadso', 'Santiago'], ['Pijao', 'Candelaria'], ['SupÃ\xada', 'La Playa de BelÃ©n'], ['San Carlos', 'La MontaÃ±ita'], ['El Retorno', 'PulÃ\xad']], max_length=100),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='idPaciente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]