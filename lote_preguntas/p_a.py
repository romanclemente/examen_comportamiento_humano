import uuid

questions = {
    f"2{str(uuid.uuid4())} ¿Cuál de las siguientes técnicas se basa en el registro de la actividad eléctrica de las neuronas de la corteza cerebral de manera externa?": {
        "v": "Electroencefalografía (EEG)",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Resonancia magnética funcional (RMf)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"3{str(uuid.uuid4())} ¿Qué componente del sistema nervioso periférico conecta el SNC con las estructuras de la cabeza?": {
        "v": "Nervios craneales",
        "f": ["Nervios espinales", "Nervios autónomos", "Nervios somáticos"],
    },
    f"4{str(uuid.uuid4())} ¿Cuál es el objetivo principal de la neurociencia cognitiva?": {
        "v": "Comprender los mecanismos neurales del comportamiento y procesos psicológicos",
        "f": [
            "Estudiar la estructura anatómica del cerebro",
            "Investigar la evolución del sistema nervioso",
            "Desarrollar tratamientos para enfermedades mentales",
        ],
    },
    f"5{str(uuid.uuid4())} ¿Qué término se refiere a las conexiones nerviosas por las que una estructura nerviosa recibe información de otras estructuras?": {
        "v": "Aferencia",
        "f": ["Eferencia", "Sinapsis", "Neurotransmisión"],
    },
    f"6{str(uuid.uuid4())} ¿Cuál es la función principal del sistema nervioso autónomo?": {
        "v": "Controlar funciones involuntarias",
        "f": [
            "Controlar funciones voluntarias",
            "Procesar información sensorial",
            "Coordinar movimientos corporales",
        ],
    },
    f"7{str(uuid.uuid4())} ¿Cuál de los siguientes no es un principio básico de la investigación científica?": {
        "v": "Subjetiva",
        "f": ["Sistemática", "Reproducible", "Empírica"],
    },
    f"8{str(uuid.uuid4())} ¿Qué técnica de neuroimagen permite observar el funcionamiento del cerebro sin necesidad de producir una lesión?": {
        "v": "Resonancia magnética funcional (RMf)",
        "f": [
            "Microscopía",
            "Tomografía por emisión de positrones (TEP)",
            "Electroencefalografía (EEG)",
        ],
    },
    f"9{str(uuid.uuid4())} ¿Qué tipo de información es más fácil de vincular con el concepto de aferencia?": {
        "v": "Estímulos sensoriales",
        "f": ["Órdenes motoras", "Respuestas emocionales", "Activación muscular"],
    },
    f"10{str(uuid.uuid4())} ¿Qué enfoque de división del sistema nervioso considera la estructura física sin importar su funcionalidad?": {
        "v": "División anatómica",
        "f": ["División funcional", "División fisiológica", "División cognitiva"],
    },
    f"11{str(uuid.uuid4())} ¿Qué estructura del sistema nervioso humano incluye el cerebro, el tronco encefálico y el cerebelo?": {
        "v": "Encéfalo",
        "f": [
            "Sistema nervioso periférico",
            "Sistema nervioso autónomo",
            "Médula espinal",
        ],
    },
    f"12{str(uuid.uuid4())} ¿Qué término describe la capacidad del cerebro para cambiar y adaptarse a lo largo del tiempo?": {
        "v": "Neuroplasticidad",
        "f": ["Plasticidad sináptica", "Sinapsis", "Neurogenesis"],
    },
    f"13{str(uuid.uuid4())} ¿Cuál es una característica del sistema nervioso somático?": {
        "v": "Inerva músculos estriados y piel",
        "f": [
            "Controla músculos lisos y glándulas",
            "Regula funciones involuntarias",
            "Controla el ritmo cardíaco",
        ],
    },
    f"14{str(uuid.uuid4())} ¿Qué tipo de investigación busca encontrar una relación entre dos o más variables sin determinar causalidad?": {
        "v": "Correlacional",
        "f": ["Experimental", "Descriptiva", "Explicativa"],
    },
    f"15{str(uuid.uuid4())} ¿Qué técnica permite medir el consumo de oxígeno en el cerebro para generar imágenes funcionales?": {
        "v": "Resonancia magnética funcional (RMf)",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Electroencefalografía (EEG)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"16{str(uuid.uuid4())} ¿Qué tipo de división del sistema nervioso considera la funcionalidad sin importar la ubicación física de los componentes?": {
        "v": "División funcional",
        "f": ["División anatómica", "División espacial", "División morfológica"],
    },
    f"17{str(uuid.uuid4())} ¿Qué componente del sistema nervioso periférico conecta el SNC con las estructuras periféricas del cuerpo?": {
        "v": "Nervios espinales",
        "f": ["Nervios craneales", "Nervios autónomos", "Nervios somáticos"],
    },
    f"18{str(uuid.uuid4())} ¿Qué técnica se utiliza para observar las conexiones neuronales y su organización en circuitos específicos?": {
        "v": "Tractografía por tensor de difusión (TD)",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Resonancia magnética funcional (RMf)",
            "Electroencefalografía (EEG)",
        ],
    },
    f"19{str(uuid.uuid4())} ¿Qué tipo de investigación se realiza sin entrar en hipótesis específicas y busca observar cómo se manifiesta la realidad?": {
        "v": "Exploratoria",
        "f": ["Experimental", "Descriptiva", "Explicativa"],
    },
    f"20{str(uuid.uuid4())} ¿Qué técnica de neuroimagen utiliza sustancias marcadas radioactivamente para rastrear índices metabólicos?": {
        "v": "Tomografía por emisión de positrones (TEP)",
        "f": [
            "Resonancia magnética funcional (RMf)",
            "Electroencefalografía (EEG)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"21{str(uuid.uuid4())} ¿Qué término se refiere a las conexiones nerviosas por las que una estructura nerviosa envía información a otras estructuras?": {
        "v": "Eferencia",
        "f": ["Sinapsis", "Aferencia", "Neurotransmisión"],
    },
    f"22{str(uuid.uuid4())} ¿Cuál de las siguientes es una técnica basada en la estimulación de áreas específicas del cerebro para observar efectos conductuales?": {
        "v": "Estimulación eléctrica cortical",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Resonancia magnética funcional (RMf)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"23{str(uuid.uuid4())} ¿Qué tipo de información es más fácil de vincular con el concepto de eferencia?": {
        "v": "Órdenes motoras",
        "f": ["Estímulos sensoriales", "Respuestas emocionales", "Activación cerebral"],
    },
    f"24{str(uuid.uuid4())} ¿Qué división del sistema nervioso incluye el encéfalo y la médula espinal?": {
        "v": "Sistema nervioso central",
        "f": [
            "Sistema nervioso somático",
            "Sistema nervioso periférico",
            "Sistema nervioso autónomo",
        ],
    },
    f"25{str(uuid.uuid4())} ¿Qué estructura del encéfalo es responsable de la modulación del movimiento?": {
        "v": "Ganglios basales",
        "f": ["Cerebelo", "Corteza motora primaria", "Tronco encefálico"],
    },
    f"26{str(uuid.uuid4())} ¿Qué técnica se basa en la detección de campos magnéticos generados por la actividad neuronal?": {
        "v": "Magnetoencefalografía (MEG)",
        "f": [
            "Resonancia magnética funcional (RMf)",
            "Electroencefalografía (EEG)",
            "Tomografía por emisión de positrones (TEP)",
        ],
    },
    f"27{str(uuid.uuid4())} ¿Qué tipo de investigación busca describir formalmente cómo se manifiesta un fenómeno científico, natural o social?": {
        "v": "Descriptiva",
        "f": ["Experimental", "Correlacional", "Explicativa"],
    },
    f"28{str(uuid.uuid4())} ¿Qué término se refiere a los sentidos que proveen información sobre el estado interno del organismo?": {
        "v": "Interoceptivos",
        "f": ["Exteroceptivos", "Proprioceptivos", "Viscerales"],
    },
    f"29{str(uuid.uuid4())} ¿Cuál de las siguientes técnicas no se utiliza para el estudio in vivo del cerebro?": {
        "v": "Microscopía",
        "f": [
            "Electroencefalografía (EEG)",
            "Tomografía por emisión de positrones (TEP)",
            "Resonancia magnética funcional (RMf)",
        ],
    },
    f"30{str(uuid.uuid4())} ¿Qué tipo de diseño de investigación implica la observación intensiva de un solo caso específico?": {
        "v": "Estudio de caso único",
        "f": ["Estudio experimental", "Estudio cuasiexperimental", "Encuesta"],
    },
    f"31{str(uuid.uuid4())} ¿Qué componente del sistema nervioso autónomo controla las funciones de los órganos internos y los vasos sanguíneos?": {
        "v": "Nervios autónomos",
        "f": ["Nervios craneales", "Nervios espinales", "Nervios somáticos"],
    },
    f"32{str(uuid.uuid4())} ¿Qué técnica permite estudiar la comunicación entre áreas del cerebro rastreando el movimiento de partículas?": {
        "v": "Tractografía por tensor de difusión (TD)",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Resonancia magnética funcional (RMf)",
            "Electroencefalografía (EEG)",
        ],
    },
    f"33{str(uuid.uuid4())} ¿Cuál es el propósito principal del sistema nervioso somático?": {
        "v": "Controlar funciones voluntarias",
        "f": [
            "Controlar funciones involuntarias",
            "Procesar información sensorial",
            "Regular el ritmo cardíaco",
        ],
    },
    f"34{str(uuid.uuid4())} ¿Qué técnica se utiliza para estimular eléctricamente zonas específicas del cerebro para observar efectos conductuales?": {
        "v": "Estimulación magnética transcraneal (EMT)",
        "f": [
            "Electroencefalografía (EEG)",
            "Resonancia magnética funcional (RMf)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"35{str(uuid.uuid4())} ¿Qué término se refiere a los sentidos que proporcionan información sobre el ambiente externo?": {
        "v": "Exteroceptivos",
        "f": ["Interoceptivos", "Proprioceptivos", "Viscerales"],
    },
    f"36{str(uuid.uuid4())} ¿Cuál es una característica del sistema nervioso autónomo?": {
        "v": "Controla funciones involuntarias",
        "f": [
            "Controla músculos estriados y piel",
            "Regula funciones voluntarias",
            "Coordina movimientos corporales",
        ],
    },
    f"37{str(uuid.uuid4())} ¿Qué tipo de investigación busca detectar que dos variables se relacionen de manera causal?": {
        "v": "Explicativa",
        "f": ["Experimental", "Descriptiva", "Correlacional"],
    },
    f"38{str(uuid.uuid4())} ¿Qué estructura del sistema nervioso central incluye el cerebro, el tronco encefálico y el cerebelo?": {
        "v": "Encéfalo",
        "f": [
            "Sistema nervioso periférico",
            "Sistema nervioso autónomo",
            "Médula espinal",
        ],
    },
    f"39{str(uuid.uuid4())} ¿Qué técnica de neuroimagen permite observar el funcionamiento del cerebro mediante la detección de variaciones en el consumo de oxígeno?": {
        "v": "Resonancia magnética funcional (RMf)",
        "f": [
            "Tomografía por emisión de positrones (TEP)",
            "Electroencefalografía (EEG)",
            "Magnetoencefalografía (MEG)",
        ],
    },
    f"40{str(uuid.uuid4())} ¿Qué término describe la capacidad del cerebro para cambiar y adaptarse a lo largo del tiempo?": {
        "v": "Neuroplasticidad",
        "f": ["Plasticidad sináptica", "Sinapsis", "Neurogenesis"],
    },
    f"{str(uuid.uuid4())}¿Qué es la neurociencia?": {
        "v": "Es el estudio sistemático del sistema nervioso.",
        "f": [
            "Es el estudio del sistema cardiovascular.",
            "Es el estudio de los sistemas computacionales.",
            "Es el estudio del comportamiento animal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué función tiene el sistema nervioso?": {
        "v": "Permite percibir información y emitir respuestas.",
        "f": [
            "Controla únicamente el sistema digestivo.",
            "Regula solo la circulación sanguínea.",
            "Es responsable de la reproducción celular.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tipo de sistemas nerviosos tienen las medusas y las estrellas de mar?": {
        "v": "Tienen redes nerviosas dispersas.",
        "f": [
            "Tienen un cerebro centralizado.",
            "Carecen totalmente de sistema nervioso.",
            "Tienen médulas espinales desarrolladas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo perciben información las plantas?": {
        "v": "Detectan información lumínica para crecer.",
        "f": [
            "A través de un sistema nervioso complejo.",
            "Utilizan órganos auditivos para detectar sonidos.",
            "Detectan información térmica para florecer.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué mecanismo de desplazamiento utilizan los espermatozoides?": {
        "v": "Se desplazan con flagelos.",
        "f": [
            "Utilizan cilios para moverse.",
            "Se desplazan mediante pseudópodos.",
            "Utilizan contracciones musculares para moverse.",
        ],
    },
    f"{str(uuid.uuid4())}¿En qué se diferencia un sistema computacional de un sistema nervioso?": {
        "v": "Los sistemas computacionales perciben información y emiten respuestas, pero no tienen un sistema nervioso.",
        "f": [
            "Los sistemas computacionales no pueden percibir información.",
            "Los sistemas computacionales tienen neuronas digitales.",
            "Los sistemas computacionales funcionan con impulsos nerviosos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Por qué es complejo el sistema nervioso humano?": {
        "v": "Debido a la gran cantidad de conexiones y funciones que realiza.",
        "f": [
            "Porque es más grande que otros sistemas nerviosos.",
            "Porque está compuesto únicamente por neuronas motoras.",
            "Porque no puede adaptarse a cambios en el entorno.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué estudia la neurociencia cognitiva?": {
        "v": "Los mecanismos neurales que subyacen al comportamiento y procesos psicológicos humanos.",
        "f": [
            "Los procesos digestivos en humanos.",
            "La evolución de las especies marinas.",
            "Las funciones del sistema cardiovascular.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo contribuye la neurociencia a la inteligencia artificial (IA)?": {
        "v": "Inspira la creación y mejora de sistemas artificiales basados en modelos nerviosos y cognitivos.",
        "f": [
            "Limita el desarrollo de algoritmos complejos.",
            "Desvía el estudio de la robótica.",
            "Prohíbe la implementación de modelos computacionales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el Procesamiento Distribuido en Paralelo (P.D.P.)?": {
        "v": "Es la coordinación y simultaneidad de redes neuronales para computar cognición y comportamiento.",
        "f": [
            "Es un método de transmisión de datos en serie.",
            "Es una técnica exclusiva de la biología celular.",
            "Es una función del sistema digestivo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué relación histórica tiene la neurociencia cognitiva con la filosofía?": {
        "v": "La ciencia moderna, incluyendo la neurociencia, tiene sus raíces en la filosofía, especialmente desde la Grecia Clásica.",
        "f": [
            "No tiene ninguna relación con la filosofía.",
            "Se desarrolló independientemente de cualquier influencia filosófica.",
            "Surge exclusivamente de estudios modernos en biología.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué diferencia hay entre dualismo y monismo?": {
        "v": "El dualismo sostiene que mente y cuerpo están separados; el monismo sostiene que son parte de la misma realidad material.",
        "f": [
            "El dualismo es un concepto biológico, mientras que el monismo es psicológico.",
            "Ambos conceptos indican que mente y cuerpo son idénticos.",
            "El monismo sugiere que la mente no existe.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué enfoque utiliza la neurociencia para estudiar la relación entre el sistema nervioso y la cognición/conducta?": {
        "v": "Un enfoque empírico y monista.",
        "f": [
            "Un enfoque puramente teórico.",
            "Un enfoque exclusivamente dualista.",
            "Un enfoque anecdótico y especulativo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué hito importante ocurrió en 1879?": {
        "v": "La creación del Laboratorio de Psicología Experimental por Wundt.",
        "f": [
            "La invención del microscopio.",
            "El descubrimiento del ADN.",
            "La teoría de la evolución por selección natural.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué descubrió Pavlov en 1890?": {
        "v": "La Ley del Reflejo Condicionado.",
        "f": [
            "La estructura del ADN.",
            "La teoría del apego.",
            "La dinámica de fluidos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Quién inventó el encefalograma y cuándo?": {
        "v": "Hans Berger en 1937.",
        "f": [
            "Sigmund Freud en 1920.",
            "Wilhelm Wundt en 1879.",
            "Ivan Pavlov en 1890.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué publicación importante hizo Alan Turing en 1950?": {
        "v": "El Test de Turing.",
        "f": [
            "La teoría de la relatividad.",
            "El manifiesto comunista.",
            "El origen de las especies.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se logró en 2001 en el campo de la genética?": {
        "v": "La decodificación del Genoma Humano.",
        "f": [
            "El descubrimiento de la penicilina.",
            "La teoría de la relatividad.",
            "La invención del microscopio electrónico.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué significa generalización en el contexto de la neurociencia cognitiva?": {
        "v": "Explicación amplia basada en observaciones concretas.",
        "f": [
            "Una hipótesis sin datos.",
            "Un error sistemático en los experimentos.",
            "Una observación individual sin contexto.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es reducción en el contexto de la neurociencia cognitiva?": {
        "v": "Explicación de fenómenos complejos mediante fenómenos más simples.",
        "f": [
            "Ampliación de datos sin relación.",
            "Hipótesis basadas en observaciones sin datos.",
            "Conclusiones obtenidas sin experimentación.",
        ],
    },
    f"{str(uuid.uuid4())}¿Por qué es importante evitar el reduccionismo excesivo en neurociencia?": {
        "v": "Para describir comportamientos y correlacionarlos con eventos fisiológicos sin simplificar en exceso.",
        "f": [
            "Para aumentar la complejidad de los estudios.",
            "Para mantener los estudios únicamente teóricos.",
            "Para evitar la investigación empírica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se puede estudiar desde un enfoque motor y funcional en neurociencia?": {
        "v": "El movimiento del brazo humano, analizando sus movimientos y funciones.",
        "f": [
            "La estructura del ADN.",
            "Los procesos digestivos.",
            "La evolución de las especies marinas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué disciplinas están involucradas en el enfoque multidisciplinar de la neurociencia cognitiva?": {
        "v": "Biología, Psicología, Química, Física, Bioquímica, entre otras.",
        "f": [
            "Astronomía, Geología, Meteorología.",
            "Historia, Sociología, Antropología.",
            "Literatura, Música, Arte.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué niveles de abstracción se consideran en la neurociencia cognitiva?": {
        "v": "Interacción entre materia, energía, espacio y tiempo; interacción bioquímica entre moléculas; procesos e interconexiones neuronales; mente y comportamiento.",
        "f": [
            "Sistemas solares y galaxias.",
            "Únicamente procesos psicológicos.",
            "Solo interacciones entre planetas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es una interfaz cerebro-ordenador (BCI)?": {
        "v": "Es una tecnología que mejora la interacción entre humanos y máquinas.",
        "f": [
            "Es un sistema que convierte datos en imágenes.",
            "Es una técnica de terapia cognitiva.",
            "Es un tipo de hardware para videojuegos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué importancia tienen las neuronas espejo?": {
        "v": "Son cruciales en el comportamiento social.",
        "f": [
            "Son irrelevantes para la cognición.",
            "Solo funcionan en animales no humanos.",
            "No tienen ninguna función conocida.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué descubrimiento relacionado con el sistema de posicionamiento espacial fue premiado con el Nobel en 2014?": {
        "v": "La identificación de cómo el cerebro calcula la ubicación en el espacio.",
        "f": [
            "El descubrimiento del ADN.",
            "La teoría de la relatividad.",
            "El desarrollo de la teoría cuántica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo contribuyen los conocimientos en neurociencia al diseño de sistemas de IA?": {
        "v": "Permiten crear sistemas de IA más eficaces.",
        "f": [
            "Impedir el desarrollo de algoritmos.",
            "Limitar la capacidad de aprendizaje.",
            "Reducir la velocidad de procesamiento.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo puede la IA contribuir a la neurociencia?": {
        "v": "Refinando los modelos neurocientíficos basados en teorías neurobiológicas.",
        "f": [
            "Eliminando la necesidad de estudios empíricos.",
            "Sustituyendo a los investigadores humanos.",
            "Limitando el desarrollo de nuevas teorías.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se entiende por bioinspiración en el contexto de la neurociencia y la IA?": {
        "v": "Es la mejora de sistemas computacionales mediante la inspiración en el cerebro y comportamiento humanos.",
        "f": [
            "El uso de plantas en la creación de circuitos.",
            "La construcción de robots basados en insectos.",
            "El diseño de aviones inspirados en aves.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué caracteriza a la investigación científica sistemática?": {
        "v": "Es unificada en la forma de abordar problemas de estudio.",
        "f": [
            "Depende del azar en la obtención de datos.",
            "No sigue un procedimiento claro.",
            "Se basa en suposiciones no verificadas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué significa que una investigación sea controlada?": {
        "v": "Caracteriza y manipula variables de manera definida y ordenada.",
        "f": [
            "No considera las variables del estudio.",
            "Se realiza sin una planificación previa.",
            "No establece diferencias claras entre variables.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la base de una investigación empírica?": {
        "v": "La experimentación.",
        "f": ["La especulación.", "La teoría sin pruebas.", "El análisis subjetivo."],
    },
    f"{str(uuid.uuid4())}¿Qué implica que una investigación sea racional-crítica?": {
        "v": "Deriva hipótesis de observaciones y propone nuevas hipótesis creativamente.",
        "f": [
            "Se basa únicamente en creencias personales.",
            "No permite cuestionar las hipótesis.",
            "Evita el análisis detallado de observaciones.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se busca evitar mediante la rigurosidad en la investigación científica?": {
        "v": "Interpretaciones erróneas.",
        "f": [
            "Resultados esperados.",
            "Confirmación de teorías preestablecidas.",
            "Datos aleatorios.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué característica debe cumplir una investigación para ser reproducible?": {
        "v": "Los mismos experimentos deben producir los mismos resultados si se replican bajo las mismas condiciones.",
        "f": [
            "Los resultados deben variar en cada replicación.",
            "No se debe poder replicar los experimentos.",
            "Depende de la interpretación personal del investigador.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el primer paso en el planteamiento protocolizado de una investigación?": {
        "v": "Formular una hipótesis.",
        "f": [
            "Reunir datos aleatorios.",
            "Publicar resultados preliminares.",
            "Ignorar las hipótesis iniciales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué objetivo tiene el diseño en una investigación?": {
        "v": "Planificar la secuencia de pasos de la investigación.",
        "f": [
            "Evitar la planificación previa.",
            "Alterar el orden de los pasos según conveniencia.",
            "Ignorar la estructura de la investigación.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se entiende por población en una investigación científica?": {
        "v": "Los seres u objetos naturales a estudiar.",
        "f": [
            "Los investigadores involucrados.",
            "El entorno de la investigación.",
            "Las hipótesis formuladas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué son las variables a analizar en una investigación?": {
        "v": "Magnitudes específicas y operativas de la hipótesis.",
        "f": [
            "Elementos irrelevantes al estudio.",
            "Resultados esperados.",
            "Factores no medibles.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué implica la recogida de datos en una investigación?": {
        "v": "El método para obtener los datos necesarios.",
        "f": [
            "Ignorar los métodos de obtención de datos.",
            "Depender de suposiciones sin datos.",
            "Recoger datos no relacionados con la hipótesis.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se realiza en el procesamiento de datos en una investigación?": {
        "v": "Aplicar una metodología estadística.",
        "f": [
            "Ignorar el análisis de datos.",
            "Revisar los datos superficialmente.",
            "Modificar los datos sin análisis.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el propósito de la interpretación de datos en una investigación?": {
        "v": "Asegurar que los datos reflejan la realidad buscada.",
        "f": [
            "Proponer nuevas hipótesis sin datos.",
            "Alterar los datos según la hipótesis.",
            "Evitar la interpretación de los datos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se busca con la conclusión de una investigación?": {
        "v": "Formalizar la aceptación o descarte de la hipótesis.",
        "f": [
            "Presentar hipótesis sin análisis.",
            "Cambiar la hipótesis según resultados.",
            "Ignorar los resultados obtenidos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se hace en la comunicación de resultados de una investigación?": {
        "v": "Difundir los resultados a la comunidad científica.",
        "f": [
            "Mantener los resultados en secreto.",
            "Alterar los resultados para publicarlos.",
            "Evitar la difusión de los resultados.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué caracteriza a una investigación exploratoria?": {
        "v": "Observación sin hipótesis específicas.",
        "f": [
            "Formular hipótesis antes de observar.",
            "Confirmar hipótesis establecidas.",
            "Evitar la observación detallada.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tipo de investigación implica la medición formal de fenómenos?": {
        "v": "Descriptiva.",
        "f": ["Exploratoria.", "Cualitativa.", "Teórica."],
    },
    f"{str(uuid.uuid4())}¿Qué estudia una investigación correlacional?": {
        "v": "La relación entre dos o más variables.",
        "f": [
            "La causa de un solo fenómeno.",
            "La historia de un fenómeno.",
            "La definición de conceptos teóricos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el objetivo de una investigación explicativa?": {
        "v": "Establecer una relación causal entre variables.",
        "f": [
            "Describir fenómenos sin análisis.",
            "Observar sin formular hipótesis.",
            "Ignorar las relaciones causales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué debe respetar la ética en la investigación científica?": {
        "v": "La libertad individual y adherirse a parámetros morales.",
        "f": [
            "Los intereses económicos.",
            "Las opiniones personales del investigador.",
            "La manipulación de datos para favorecer resultados.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué estudian los estudios fisiológicos?": {
        "v": "El funcionamiento biológico/fisiológico del organismo.",
        "f": [
            "El comportamiento humano.",
            "Las relaciones sociales.",
            "Las estructuras políticas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué estudian los estudios conductuales?": {
        "v": "Aspectos del comportamiento humano bajo ciertas circunstancias.",
        "f": [
            "Las funciones biológicas del organismo.",
            "Los fenómenos naturales.",
            "Los procesos químicos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué define el diseño de investigación?": {
        "v": "La planificación del esquema general de la investigación.",
        "f": [
            "La recolección de datos aleatorios.",
            "La interpretación de resultados sin análisis.",
            "La publicación de resultados preliminares.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué determina un diseño de investigación en términos de variables?": {
        "v": "Las variables dependientes e independientes.",
        "f": [
            "Las conclusiones del estudio.",
            "La metodología sin considerar variables.",
            "Los resultados esperados.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se entiende por técnicas de investigación?": {
        "v": "Materiales, herramientas y tecnologías necesarias para la investigación.",
        "f": [
            "Las hipótesis formuladas.",
            "Los resultados obtenidos.",
            "Las conclusiones del estudio.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué caracteriza a los diseños experimentales?": {
        "v": "La existencia de un grupo experimental y un grupo control.",
        "f": [
            "La falta de control de variables.",
            "El estudio de un solo caso.",
            "La observación sin intervención.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué diferencia a los diseños cuasiexperimentales?": {
        "v": "No controlan todas las variables.",
        "f": [
            "Controlan todas las variables.",
            "No consideran ningún grupo control.",
            "No manipulan ninguna variable.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tipo de estudio se centra en un solo caso intensivamente?": {
        "v": "Estudio de caso único.",
        "f": [
            "Estudio correlacional.",
            "Estudio experimental.",
            "Estudio descriptivo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué método utiliza la electroencefalografía (EEG)?": {
        "v": "Registro de la actividad eléctrica de las neuronas corticales.",
        "f": [
            "Medición de la actividad muscular.",
            "Evaluación de la respuesta cardíaca.",
            "Observación del comportamiento externo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué impacto tienen las interfaces cerebro-ordenador (BCI)?": {
        "v": "Mejorar la interacción entre humanos y máquinas.",
        "f": [
            "Reducir la capacidad cognitiva humana.",
            "Aumentar la distancia entre humanos y tecnología.",
            "Limitar las funciones de las máquinas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la finalidad de las técnicas anatómicas en el estudio del comportamiento humano?": {
        "v": "Identificación y diferenciación de estructuras cerebrales y un enfoque estructural del sistema nervioso.",
        "f": [
            "Medir la actividad eléctrica del cerebro.",
            "Detectar variaciones en el consumo de oxígeno.",
            "Estudiar la comunicación entre áreas del cerebro.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se observa con la microscopía?": {
        "v": "Muestras delgadas de tejido nervioso.",
        "f": [
            "Imágenes del cerebro en 3D.",
            "Cambios en el potencial eléctrico de las neuronas.",
            "Niveles de oxigenación de la sangre.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué instrumentos se utilizan en la microscopía?": {
        "v": "Microtomos, vibratomos, criostatos, microscopios electrónicos, entre otros.",
        "f": [
            "Electrodos invasivos, escáneres PET, resonadores magnéticos.",
            "Cámaras de alta velocidad, detectores de rayos gamma, fotodiodos.",
            "Sensores de temperatura, analizadores de gases, espectrofotómetros.",
        ],
    },
    f"{str(uuid.uuid4())}¿Por qué es importante la tinción en las técnicas microscópicas?": {
        "v": "Para distinguir estructuras celulares.",
        "f": [
            "Para medir la actividad cerebral.",
            "Para obtener imágenes tridimensionales.",
            "Para registrar la actividad eléctrica de las neuronas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué permite distinguir las técnicas histoquímicas?": {
        "v": "Estructuras celulares mediante compuestos químicos.",
        "f": [
            "Niveles de actividad cerebral.",
            "Cambios en el potencial eléctrico.",
            "Concentraciones de neurotransmisores.",
        ],
    },
    "Proporcione un ejemplo de una técnica histoquímica.": {
        "v": "La tinción de Nissl.",
        "f": [
            "Electroencefalografía (EEG).",
            "Resonancia Magnética funcional (RMf).",
            "Tomografía Axial Computarizada (TAC).",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se utiliza en las técnicas inmunohistoquímicas para distinguir tejidos?": {
        "v": "Anticuerpos fluorescentes.",
        "f": ["Electrodos invasivos.", "Rayos X.", "Campos magnéticos."],
    },
    f"{str(uuid.uuid4())}¿Qué es la hibridación in situ?": {
        "v": "Uso de sondas de ADN o ARN para estudiar proteínas específicas.",
        "f": [
            "Medición de potenciales eléctricos neuronales.",
            "Obtención de imágenes por resonancia magnética.",
            "Registro de actividad cerebral mediante EEG.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tecnología utiliza rayos X para obtener imágenes del cerebro?": {
        "v": "TAC (Tomografía Axial Computarizada).",
        "f": [
            "RMN (Resonancia Magnética Nuclear).",
            "MEG (Magnetoencefalografía).",
            "TEP (Tomografía por Emisión de Positrones).",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son las ventajas del TAC?": {
        "v": "Imágenes en 2D y 3D, y bajo coste.",
        "f": [
            "Alta resolución espacial.",
            "Detección de actividad eléctrica.",
            "Análisis de composición química de tejidos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son las desventajas del TAC?": {
        "v": "Radiación, invasividad, y menor resolución comparada con técnicas modernas.",
        "f": [
            "Coste elevado, imágenes en blanco y negro, complejidad técnica.",
            "Alta resolución temporal, no invasivo, caro.",
            "Requiere anestesia, baja disponibilidad, no portátil.",
        ],
    },
    f"{str(uuid.uuid4())}¿En qué se basa la RMN (Resonancia Magnética Nuclear)?": {
        "v": "En la abundancia de protones H+ en el tejido nervioso.",
        "f": [
            "En la emisión de positrones.",
            "En la actividad eléctrica de las neuronas.",
            "En la conductancia de la piel.",
        ],
    },
    "Mencione una ventaja de la RMN.": {
        "v": "Detección de lesiones en imágenes en 2D y 3D.",
        "f": [
            "Medición de actividad eléctrica.",
            "Bajo coste y portabilidad.",
            "Alta resolución temporal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es una desventaja de la RMN?": {
        "v": "Coste elevado y menor resolución temporal que espacial.",
        "f": ["Alta radiación.", "Imágenes solo en 2D.", "Invasividad."],
    },
    f"{str(uuid.uuid4())}¿Cuál es la finalidad de las técnicas neurofisiológicas?": {
        "v": "Captura de correlatos fisiológicos de la actividad cognitiva.",
        "f": [
            "Obtención de imágenes anatómicas.",
            "Medición de niveles de oxigenación de la sangre.",
            "Análisis de la estructura química del tejido cerebral.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué se mide con el uso de microelectrodos en las técnicas neurofisiológicas?": {
        "v": "Cambios de potencial eléctrico de las neuronas.",
        "f": [
            "Niveles de glucosa en el cerebro.",
            "Flujo sanguíneo cerebral.",
            "Producción de neurotransmisores.",
        ],
    },
    f"{str(uuid.uuid4())}¿Para qué se utiliza la estimulación eléctrica de zonas corticales?": {
        "v": "Para observar efectos conductuales y minimizar daño funcional en neurocirugía.",
        "f": [
            "Para obtener imágenes cerebrales.",
            "Para medir la actividad metabólica.",
            "Para registrar la conductancia de la piel.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué mide la psicofisiología periférica?": {
        "v": "Efectos de procesos cognitivos y emocionales en estructuras externas.",
        "f": [
            "Actividad eléctrica cerebral.",
            "Niveles de neurotransmisores.",
            "Flujo sanguíneo cerebral.",
        ],
    },
    "Mencione un ejemplo de psicofisiología periférica.": {
        "v": "SCR (Skin Conductance Response), que se relaciona con experiencias emocionales.",
        "f": [
            "EEG (Electroencefalografía).",
            "TEP (Tomografía por Emisión de Positrones).",
            "RMf (Resonancia Magnética funcional).",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué indica el nivel de oxigenación de la sangre en psicofisiología periférica?": {
        "v": "Actividad cognitiva y emocional.",
        "f": [
            "Conductancia de la piel.",
            "Flujo de iones a través de la membrana celular.",
            "Producción de neurotransmisores.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la finalidad de las técnicas funcionales?": {
        "v": "Estudio del funcionamiento del cerebro in vivo.",
        "f": [
            "Análisis de la estructura anatómica.",
            "Detección de potenciales eléctricos.",
            "Medición de conductancia de la piel.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué mide la resolución espacial en las técnicas funcionales?": {
        "v": "La precisión en la localización de la actividad cerebral.",
        "f": [
            "La rapidez de detección de cambios.",
            "La intensidad de la señal eléctrica.",
            "La frecuencia de los impulsos nerviosos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué mide la resolución temporal en las técnicas funcionales?": {
        "v": "La precisión en la detección del momento de la actividad cerebral.",
        "f": [
            "La localización exacta de la actividad cerebral.",
            "La intensidad de la actividad eléctrica.",
            "La cantidad de neurotransmisores liberados.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué registra la electroencefalografía (EEG)?": {
        "v": "La actividad eléctrica del cerebro.",
        "f": [
            "La estructura anatómica del cerebro.",
            "La conductancia de la piel.",
            "El flujo sanguíneo cerebral.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tipo de resolución tiene el EEG?": {
        "v": "Alta resolución temporal y baja resolución espacial.",
        "f": [
            "Alta resolución espacial y baja resolución temporal.",
            "Alta resolución tanto espacial como temporal.",
            "Baja resolución espacial y temporal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué técnica utiliza campos magnéticos para estudiar la actividad cerebral?": {
        "v": "Magnetoencefalografía (MEG).",
        "f": [
            "Resonancia Magnética funcional (RMf).",
            "Tomografía por Emisión de Positrones (TEP).",
            "Electroencefalografía (EEG).",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué permite observar la Tomografía por Emisión de Positrones (TEP)?": {
        "v": "El funcionamiento cerebral mediante índices metabólicos.",
        "f": [
            "La actividad eléctrica del cerebro.",
            "La estructura anatómica del cerebro.",
            "El flujo sanguíneo cerebral.",
        ],
    },
    f"{str(uuid.uuid4())}¿En qué se basa la Resonancia Magnética funcional (RMf)?": {
        "v": "En la técnica BOLD para detectar variaciones en el consumo de oxígeno.",
        "f": [
            "En la emisión de positrones.",
            "En la actividad eléctrica de las neuronas.",
            "En la conductancia de la piel.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué estudia la Tractografía por Tensor de Difusión (TD)?": {
        "v": "La comunicación entre áreas del cerebro.",
        "f": [
            "La actividad metabólica del cerebro.",
            "La estructura anatómica del cerebro.",
            "La conductancia de la piel.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo mejora la IA las tecnologías de estudio del cerebro?": {
        "v": "Mejora del funcionamiento mediante métodos de IA y uso de algoritmos de clasificación para diagnósticos y análisis.",
        "f": [
            "Incremento de la conductancia de la piel.",
            "Aumento de la emisión de positrones.",
            "Disminución del consumo de oxígeno.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el objetivo principal del tema 4?": {
        "v": "Comprender el sistema nervioso humano como la base física de la mente y el comportamiento.",
        "f": [
            "Estudiar el comportamiento humano en diferentes culturas.",
            "Analizar los procesos evolutivos del cerebro.",
            "Entender las bases genéticas del comportamiento.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué metáfora se utiliza para explicar la relación entre el sistema nervioso y la mente?": {
        "v": "La analogía computacional, donde el sistema nervioso es el hardware y la mente y el comportamiento son el software.",
        "f": [
            "La metáfora del reloj, donde el cerebro es el reloj y la mente es el tiempo.",
            "La metáfora del jardín, donde el cerebro es la tierra y la mente son las plantas.",
            "La metáfora del río, donde el cerebro es el cauce y la mente es el agua.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo se utiliza el conocimiento del cerebro humano en inteligencia artificial (IA)?": {
        "v": "Para inspirar sistemas de IA, mediante bioinspiración.",
        "f": [
            "Para replicar directamente las funciones cerebrales en robots.",
            "Para diseñar circuitos electrónicos complejos.",
            "Para estudiar el comportamiento de los animales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué diferencia existe entre modelado funcional y simulación completa del cerebro?": {
        "v": "El modelado funcional simula el software cerebral, mientras que la simulación completa imita tanto el hardware como el software del cerebro.",
        "f": [
            "El modelado funcional es más costoso que la simulación completa.",
            "La simulación completa solo se utiliza en estudios teóricos.",
            "El modelado funcional solo considera la estructura física del cerebro.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el propósito del sistema nervioso?": {
        "v": "Está diseñado para la supervivencia y perpetuación de la especie.",
        "f": [
            "Para generar impulsos eléctricos.",
            "Para almacenar información genética.",
            "Para producir hormonas y enzimas.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué ha evolucionado más rápido, la mente o el cerebro en sí mismo?": {
        "v": "La mente ha evolucionado más rápido que el cerebro.",
        "f": [
            "El cerebro ha evolucionado más rápido que la mente.",
            "Ambos han evolucionado al mismo ritmo.",
            "La evolución de ambos es irrelevante para el comportamiento humano.",
        ],
    },
    f"{str(uuid.uuid4())}¿En qué se basa la división anatómica del sistema nervioso humano?": {
        "v": "Se basa en la estructura física del sistema nervioso.",
        "f": [
            "En las funciones biológicas del sistema nervioso.",
            "En la distribución química de neurotransmisores.",
            "En la edad del individuo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son los componentes principales del sistema nervioso central (SNC)?": {
        "v": "El encéfalo (incluyendo cerebro, tronco encefálico y cerebelo) y la médula espinal.",
        "f": [
            "El sistema límbico y la corteza cerebral.",
            "Los nervios craneales y espinales.",
            "El hipotálamo y la hipófisis.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué conecta la médula espinal?": {
        "v": "Conecta el encéfalo con el sistema nervioso periférico (SNP).",
        "f": [
            "Conecta el encéfalo con los músculos del cuerpo.",
            "Conecta el sistema límbico con la corteza cerebral.",
            "Conecta las glándulas endocrinas con el cerebro.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué incluye el sistema nervioso periférico (SNP)?": {
        "v": "Tejidos nerviosos fuera del SNC, incluyendo nervios craneales y nervios espinales.",
        "f": [
            "El encéfalo y la médula espinal.",
            "Solo los nervios espinales.",
            "Solo los nervios craneales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la función de los nervios craneales?": {
        "v": "Conectar el SNC con estructuras de la cabeza.",
        "f": [
            "Controlar los movimientos voluntarios del cuerpo.",
            "Regular las funciones involuntarias del cuerpo.",
            "Transmitir información genética.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la función de los nervios espinales?": {
        "v": "Conectar el SNC con estructuras periféricas del cuerpo.",
        "f": [
            "Transmitir información visual al cerebro.",
            "Controlar la secreción de hormonas.",
            "Regular la temperatura corporal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué términos se utilizan para describir ubicaciones relativas en neuroanatomía?": {
        "v": "Ventral, dorsal, superior, inferior, caudal, rostral, medial, lateral, ipsilateral, contralateral, bilateral.",
        "f": [
            "Anterior, posterior, medial, lateral, proximal, distal.",
            "Interior, exterior, arriba, abajo, izquierda, derecha.",
            "Superficial, profundo, central, periférico, longitudinal, transversal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son los planos o cortes utilizados en neuroanatomía?": {
        "v": "Coronal, sagital, horizontal.",
        "f": [
            "Diagonal, axial, lateral.",
            "Longitudinal, transversal, oblicuo.",
            "Medial, lateral, dorsal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué ejes se utilizan en neuroanatomía?": {
        "v": "Vertical, frontal (anteroposterior), transversal.",
        "f": [
            "Diagonal, horizontal, perpendicular.",
            "Longitudinal, oblicuo, paralelo.",
            "Superior, inferior, medial.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el eje de Forel?": {
        "v": "Un eje que considera el cambio de orientación a 90° del neuroeje.",
        "f": [
            "Un eje que se mantiene constante a lo largo del cerebro.",
            "Un eje que solo se aplica al sistema nervioso periférico.",
            "Un eje utilizado únicamente en estudios de neuroquímica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el eje de Meynert?": {
        "v": "Un eje alineado con la línea de ascenso de la médula espinal, sin considerar el cambio de orientación.",
        "f": [
            "Un eje que cambia su orientación en cada segmento del cerebro.",
            "Un eje paralelo al eje de Forel.",
            "Un eje utilizado para describir la orientación de los vasos sanguíneos en el cerebro.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el objetivo principal del tema 4?": {
        "v": "Comprender el sistema nervioso humano como la base física de la mente y el comportamiento.",
        "f": [
            "Estudiar la biología celular.",
            "Analizar la evolución humana.",
            "Entender la física cuántica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué metáfora se utiliza para explicar la relación entre el sistema nervioso y la mente?": {
        "v": "La analogía computacional, donde el sistema nervioso es el hardware y la mente y el comportamiento son el software.",
        "f": [
            "La metáfora mecánica.",
            "La analogía hidráulica.",
            "La metáfora del reloj.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo se utiliza el conocimiento del cerebro humano en inteligencia artificial (IA)?": {
        "v": "Para inspirar sistemas de IA, mediante bioinspiración.",
        "f": [
            "Para diseñar circuitos electrónicos.",
            "Para crear nuevos lenguajes de programación.",
            "Para mejorar la eficiencia energética.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué diferencia existe entre modelado funcional y simulación completa del cerebro?": {
        "v": "El modelado funcional simula el software cerebral, mientras que la simulación completa imita tanto el hardware como el software del cerebro.",
        "f": [
            "No hay diferencia.",
            "El modelado funcional imita el hardware del cerebro.",
            "La simulación completa solo simula el software cerebral.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es el propósito del sistema nervioso?": {
        "v": "Está diseñado para la supervivencia y perpetuación de la especie.",
        "f": [
            "Para controlar el clima.",
            "Para regular el metabolismo.",
            "Para almacenar nutrientes.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué ha evolucionado más rápido, la mente o el cerebro en sí mismo?": {
        "v": "La mente ha evolucionado más rápido que el cerebro.",
        "f": [
            "El cerebro ha evolucionado más rápido que la mente.",
            "Ambos han evolucionado a la misma velocidad.",
            "Ninguno ha evolucionado.",
        ],
    },
    f"{str(uuid.uuid4())}¿En qué se basa la división anatómica del sistema nervioso humano?": {
        "v": "Se basa en la estructura física del sistema nervioso.",
        "f": [
            "En la función del sistema nervioso.",
            "En la edad del individuo.",
            "En la cantidad de neuronas presentes.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son los componentes principales del sistema nervioso central (SNC)?": {
        "v": "El encéfalo (incluyendo cerebro, tronco encefálico y cerebelo) y la médula espinal.",
        "f": [
            "El encéfalo y los nervios periféricos.",
            "Solo el cerebro y el cerebelo.",
            "El tronco encefálico y los nervios espinales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué conecta la médula espinal?": {
        "v": "Conecta el encéfalo con el sistema nervioso periférico (SNP).",
        "f": [
            "Conecta los músculos con los huesos.",
            "Conecta el corazón con los pulmones.",
            "Conecta las extremidades entre sí.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué incluye el sistema nervioso periférico (SNP)?": {
        "v": "Tejidos nerviosos fuera del SNC, incluyendo nervios craneales y nervios espinales.",
        "f": [
            "Solo los nervios craneales.",
            "Solo los nervios espinales.",
            "El cerebro y la médula espinal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la función de los nervios craneales?": {
        "v": "Conectar el SNC con estructuras de la cabeza.",
        "f": [
            "Conectar el corazón con el cerebro.",
            "Conectar la médula espinal con las extremidades.",
            "Conectar el sistema digestivo con el cerebro.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuál es la función de los nervios espinales?": {
        "v": "Conectar el SNC con estructuras periféricas del cuerpo.",
        "f": [
            "Conectar los órganos internos entre sí.",
            "Conectar el cerebro con el corazón.",
            "Conectar los músculos con los huesos.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué términos se utilizan para describir ubicaciones relativas en neuroanatomía?": {
        "v": "Ventral, dorsal, superior, inferior, caudal, rostral, medial, lateral, ipsilateral, contralateral, bilateral.",
        "f": [
            "Cercano, lejano, frontal, posterior.",
            "Superior, inferior, izquierdo, derecho.",
            "Central, periférico, anterior, posterior.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son los planos o cortes utilizados en neuroanatomía?": {
        "v": "Coronal, sagital, horizontal.",
        "f": [
            "Transversal, oblicuo, radial.",
            "Axial, frontal, radial.",
            "Oblicuo, tangencial, longitudinal.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué ejes se utilizan en neuroanatomía?": {
        "v": "Vertical, frontal (anteroposterior), transversal.",
        "f": [
            "Lateral, diagonal, longitudinal.",
            "Oblicuo, perpendicular, paralelo.",
            "Radial, axial, tangencial.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el eje de Forel?": {
        "v": "Un eje que considera el cambio de orientación a 90° del neuroeje.",
        "f": [
            "Un eje paralelo al eje de Meynert.",
            "Un eje sin orientación específica.",
            "Un eje utilizado en la óptica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el eje de Meynert?": {
        "v": "Un eje alineado con la línea de ascenso de la médula espinal, sin considerar el cambio de orientación.",
        "f": [
            "Un eje perpendicular al eje de Forel.",
            "Un eje utilizado en la biología celular.",
            "Un eje alineado con el corazón.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cuáles son los sistemas nerviosos principales en la división fisiológico-funcional?": {
        "v": "Sistema nervioso somático (SNS) y sistema nervioso autónomo (SNA).",
        "f": [
            "Sistema nervioso central y sistema nervioso periférico.",
            "Sistema endocrino y sistema exocrino.",
            "Sistema inmune y sistema digestivo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué inerva el sistema nervioso somático (SNS)?": {
        "v": "Músculos, piel y mucosas.",
        "f": [
            "Órganos internos y glándulas.",
            "Vasos sanguíneos y linfáticos.",
            "Tejido conectivo y adiposo.",
        ],
    },
    f"{str(uuid.uuid4())}¿Con qué funciones está relacionado el sistema nervioso somático (SNS)?": {
        "v": "Con funciones voluntarias.",
        "f": [
            "Con funciones involuntarias.",
            "Con funciones metabólicas.",
            "Con funciones hormonales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué controla el sistema nervioso autónomo (SNA)?": {
        "v": "Músculos lisos, glándulas y vasos sanguíneos.",
        "f": ["Músculos esqueléticos.", "Tejido óseo.", "Tejido cartilaginoso."],
    },
    f"{str(uuid.uuid4())}¿Con qué funciones está relacionado el sistema nervioso autónomo (SNA)?": {
        "v": "Con funciones involuntarias, como digestión y circulación.",
        "f": [
            "Con funciones voluntarias, como el movimiento.",
            "Con funciones cognitivas, como el pensamiento.",
            "Con funciones sensoriales, como la vista.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué son las aferencias en el sistema nervioso?": {
        "v": "Conexiones nerviosas que reciben información.",
        "f": [
            "Conexiones nerviosas que envían información.",
            "Conexiones nerviosas que almacenan información.",
            "Conexiones nerviosas que procesan información.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué son las eferencias en el sistema nervioso?": {
        "v": "Conexiones nerviosas que envían información.",
        "f": [
            "Conexiones nerviosas que reciben información.",
            "Conexiones nerviosas que almacenan información.",
            "Conexiones nerviosas que procesan información.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué es el sistema nervioso entérico?": {
        "v": "Una división del sistema nervioso encargada de la gestión de los músculos digestivos, distinguible por su alta autonomía.",
        "f": [
            "Una parte del sistema nervioso central.",
            "Una subdivisión del sistema nervioso somático.",
            "Un sistema nervioso exclusivo de los invertebrados.",
        ],
    },
    f"{str(uuid.uuid4())}¿Cómo es la simetría del sistema nervioso?": {
        "v": "Es bilateral, con estructuras homólogas en ambos lados.",
        "f": [
            "Es unilateral, con estructuras solo en un lado.",
            "Es radial, con estructuras distribuidas radialmente.",
            "Es asimétrica, sin una distribución clara.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué tipo de asimetría presenta el sistema nervioso?": {
        "v": "Asimetría funcional, donde funciones cognitivas involucran más áreas de un lado del cerebro que del otro.",
        "f": [
            "Asimetría estructural, con una diferencia en el tamaño de los hemisferios.",
            "Asimetría química, con diferentes neurotransmisores en cada lado.",
            "Asimetría eléctrica, con diferentes voltajes en cada hemisferio.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué analogía se utiliza para explicar la relación entre el sistema nervioso y la mente?": {
        "v": "La analogía computacional.",
        "f": [
            "La metáfora del reloj.",
            "La analogía hidráulica.",
            "La metáfora mecánica.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué estructuras están incluidas en el encéfalo?": {
        "v": "El cerebro, el tronco encefálico y el cerebelo.",
        "f": [
            "Solo el cerebro.",
            "El cerebro y los nervios craneales.",
            "El tronco encefálico y los nervios espinales.",
        ],
    },
    f"{str(uuid.uuid4())}¿Qué diferencia funcional existe entre el sistema nervioso somático y el autónomo?": {
        "v": "El SNS está relacionado con funciones voluntarias, mientras que el SNA está relacionado con funciones involuntarias.",
        "f": [
            "El SNS controla los músculos lisos y el SNA controla los músculos esqueléticos.",
            "El SNS está relacionado con funciones cognitivas y el SNA con funciones sensoriales.",
            "No hay diferencia funcional entre ambos.",
        ],
    },
}
