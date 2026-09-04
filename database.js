// AutoScale v3.5 — Database Core
// Структура: Марка → Модель → Поколение → Версия
const CAR_DATABASE = [
  {
    "id": "honda",
    "name": "Honda",
    "country": "Япония",
    "models": [
      {
        "id": "vezel",
        "name": "Vezel",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "ru",
            "name": "1 поколение",
            "code": "RU1/RU3",
            "years": "2013–2021",
            "versions": [
              {
                "id": "honda-vezel-ru1",
                "name": "1.5 бензин",
                "power": 131,
                "engine": "1.5 бензин",
                "drive": "Передний / AWD",
                "length": 4295,
                "width": 1770,
                "height": 1605,
                "wheelbase": 2610,
                "clearance": 185,
                "mass": 1180,
                "trunk": 431,
                "fuel": 6.5
              },
              {
                "id": "honda-vezel-ru3",
                "name": "Hybrid 1.5",
                "power": 152,
                "engine": "1.5 Hybrid",
                "drive": "Передний",
                "length": 4295,
                "width": 1770,
                "height": 1605,
                "wheelbase": 2610,
                "clearance": 185,
                "mass": 1260,
                "trunk": 393,
                "fuel": 4.5
              }
            ]
          }
        ]
      },
      {
        "id": "crv",
        "name": "CR-V",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "rw",
            "name": "5 поколение",
            "code": "RW",
            "years": "2017–2022",
            "versions": [
              {
                "id": "honda-crv-rw",
                "name": "1.5 Turbo",
                "power": 190,
                "engine": "1.5 Turbo",
                "drive": "Передний / AWD",
                "length": 4585,
                "width": 1855,
                "height": 1679,
                "wheelbase": 2660,
                "clearance": 208,
                "mass": 1570,
                "trunk": 561,
                "fuel": 7.5
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "toyota",
    "name": "Toyota",
    "country": "Япония",
    "models": [
      {
        "id": "chr",
        "name": "C-HR",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "ngx10",
            "name": "1 поколение",
            "code": "NGX10",
            "years": "2016–2023",
            "versions": [
              {
                "id": "toyota-chr-ngx10",
                "name": "1.2 Turbo",
                "power": 116,
                "engine": "1.2 Turbo",
                "drive": "Передний / AWD",
                "length": 4360,
                "width": 1795,
                "height": 1565,
                "wheelbase": 2640,
                "clearance": 155,
                "mass": 1390,
                "trunk": 377,
                "fuel": 6.6
              }
            ]
          }
        ]
      },
      {
        "id": "rav4",
        "name": "RAV4",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "xa50",
            "name": "5 поколение",
            "code": "XA50",
            "years": "2019–н.в.",
            "versions": [
              {
                "id": "toyota-rav4-xa50",
                "name": "2.0 бензин",
                "power": 149,
                "engine": "2.0 бензин",
                "drive": "Передний / AWD",
                "length": 4600,
                "width": 1855,
                "height": 1685,
                "wheelbase": 2690,
                "clearance": 195,
                "mass": 1540,
                "trunk": 580,
                "fuel": 7.1
              }
            ]
          }
        ]
      }
    ]
  },
  {
    "id": "volkswagen",
    "name": "Volkswagen",
    "country": "Германия",
    "models": [
      {
        "id": "troc",
        "name": "T-Roc",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "a1",
            "name": "1 поколение",
            "code": "A1",
            "years": "2017–н.в.",
            "versions": [
              {
                "id": "vw-troc-a1",
                "name": "1.5 TSI",
                "power": 150,
                "engine": "1.5 TSI",
                "drive": "Передний / AWD",
                "length": 4236,
                "width": 1819,
                "height": 1584,
                "wheelbase": 2590,
                "clearance": 160,
                "mass": 1330,
                "trunk": 445,
                "fuel": 6.4
              }
            ]
          }
        ]
      },
      {
        "id": "tiguan",
        "name": "Tiguan",
        "bodyType": "Кроссовер / SUV",
        "generations": [
          {
            "id": "ad1",
            "name": "2 поколение",
            "code": "AD1",
            "years": "2016–2024",
            "versions": [
              {
                "id": "vw-tiguan-ad1",
                "name": "2.0 TSI",
                "power": 180,
                "engine": "2.0 TSI",
                "drive": "Передний / AWD",
                "length": 4509,
                "width": 1839,
                "height": 1675,
                "wheelbase": 2677,
                "clearance": 191,
                "mass": 1650,
                "trunk": 615,
                "fuel": 8.1
              }
            ]
          }
        ]
      }
    ]
  }
];

// Преобразование иерархической базы в список для текущего движка AutoScale.
const CARS = CAR_DATABASE.flatMap(brand =>
  brand.models.flatMap(model =>
    model.generations.flatMap(generation =>
      generation.versions.map(version => ({
        ...version,
        brand: brand.name,
        brandId: brand.id,
        country: brand.country,
        model: model.name,
        modelId: model.id,
        body: model.bodyType,
        generation: generation.name,
        generationCode: generation.code,
        years: generation.years,
        trim: `${generation.code} · ${version.name} · ${version.power} л.с.`
      }))
    )
  )
);

// Вспомогательные функции для будущего селектора v4.0
const getBrands = () => CAR_DATABASE;
const getModels = brandId =>
  CAR_DATABASE.find(b => b.id === brandId)?.models || [];
const getGenerations = (brandId, modelId) =>
  getModels(brandId).find(m => m.id === modelId)?.generations || [];
const getVersions = (brandId, modelId, generationId) =>
  getGenerations(brandId, modelId).find(g => g.id === generationId)?.versions || [];
