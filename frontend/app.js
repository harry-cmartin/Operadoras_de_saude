const { createApp } = Vue

createApp({
    data() {
        return {
            searchQuery: '',
            results: [],
            debounceTimeout: null,
            loading: false
        }
    },
    methods: {
        searchOperadoras() {
            // Debounce a busca para evitar muitas requisições.
            clearTimeout(this.debounceTimeout)
            this.debounceTimeout = setTimeout(async () => {
                if (this.searchQuery.length < 2) {
                    this.results = []
                    return
                }
                
                this.loading = true
                try {
                    //TESTE FUNCIONAAAAAAAA
                    // Conectando 
                    const response = await axios.get(`http://127.0.0.1:8000/api/operadoras/?search=${encodeURIComponent(this.searchQuery)}`)
                    
                    this.results = response.data.map(item => ({
                        Registro_ANS: item.registro_ans,
                        Razao_Social: item.razao_social,
                        Nome_Fantasia: item.nome_fantasia || '-',
                        Modalidade: item.modalidade,
                        Cidade: item.cidade,
                        UF: item.uf,
                        CEP: item.cep,
                        DDD: item.ddd,
                        Telefone: item.telefone,
                        Endereco_eletronico: item.endereco_eletronico || '-',
                        Representante: item.representante
                    }))
                } catch (error) {
                    console.error('Error: ', error)
                    this.results = []
                } finally {
                    this.loading = false
                }
            }, 300)
        }
    }
}).mount('#app')
