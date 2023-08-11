<script>
    import {push} from 'svelte-spa-router'
    import {create_sympton} from '../lib/api.js'

    let _ff = ''
    let _sw = ''
    let _he = ''
    let _di = ''

    async function fast_post_sympton(event) {
        event.preventDefault()

        const _body = {
            "flushing_face": _ff,
            "sweating": _sw,
            "headache": _he,
            "dizziness": _di
        }
        
        const result = await create_sympton(_body)
        //console.log(result)

        if (result[0]){
            push('/')
        }else {

            error = result[1]
            //console.log(error)        
        }

    }

</script>
<div>
    <label for="subject">안면홍조</label>
    <input type="int" class="form-control" bind:value="{_ff}">
</div>
<div>
    <label for="subject">발한</label>
    <input type="int" class="form-control" bind:value="{_sw}">
</div>
<div>
    <label for="subject">두통</label>
    <input type="int" class="form-control" bind:value="{_he}">  
</div>
<div>
    <label for="subject">어지럼증</label>
    <input type="int" class="form-control" bind:value="{_di}">
</div>

<button class="btn btn-primary" on:click={(response) => fast_post_sympton(response)}>저장하기</button>


