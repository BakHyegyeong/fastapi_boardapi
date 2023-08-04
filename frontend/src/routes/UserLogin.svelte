<script>
    import { push } from 'svelte-spa-router'
    import { login_user } from "../lib/api.js"  
    import { access_token, user_name, is_login } from "../lib/store.js"
    
    let error = []
    let login_username = ""
    let login_password = ""

    async function fast_login(event) {
        event.preventDefault()

        const _body = {
            "username" : login_username,
            "password" : login_password,
        }

        const result = await login_user(_body)
        //console.log(result)

        if (result[0]){
            console.log(result[1])

            $access_token = result[1].access_token
            $user_name = result[1].username
            $is_login = true
            push('/')
        }else {
            error = result[1]
            //console.log(error)        
        }
        

    }
</script>

<div class="container">
    <h5 class="my-3 border-bottom pb-2">로그인</h5>
    <form method="post">
        <div class="mb-3">
            <label for="username">사용자 이름</label>
            <input type="text" class="form-control" id="username" bind:value="{login_username}">
        </div>
        <div class="mb-3">
            <label for="password">비밀번호</label>
            <input type="password" class="form-control" id="password" bind:value="{login_password}">
        </div>
        <button type="submit" class="btn btn-primary" on:click={(response) => fast_login(response)}>로그인</button>
    </form>
    <div>
        {#each error as er}
            <li>{er}</li>
        {/each}
    </div>
</div>
