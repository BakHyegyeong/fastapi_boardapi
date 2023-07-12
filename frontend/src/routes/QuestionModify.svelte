<script>
    import { push } from "svelte-spa-router";
    import Error from "../components/errorfun.js"
    import { get_question } from "../lib/api.js";
    import { update_question } from "../lib/api.js";

    export let params = {}
    let question_id = params.question_id
    let question = {}
    let error = {subject : '', content : ''}

    async function fast_get_detail() {
        question = await get_question(question_id)
    }

    fast_get_detail()

    async function fast_update_question() {

        const _body = {
            "subject" : question.subject,
            "content" : question.content,
            "question_id" : question_id
        }

        await update_question(_body)
        push('/')
    }

    function Error_check() {
        const { valid, errors_check } = Error(question.subject, question.content)
        if (valid) {
            error.subject = errors_check.subject
            error.content = errors_check.content
        } else {
            fast_update_question();
        }
    }

    
</script>

<div class="mb-3">
    <label for="subject">제목</label>
    <input type="text" class="form-control" bind:value="{question.subject}">
    <div>{error.subject}</div>
</div>
<div class="mb-3">
    <label for="content">내용</label>
    <textarea class="form-control" rows="10" bind:value="{question.content}"></textarea>
    <div>{error.content}</div>
</div>
<button class="btn btn-sm btn-outline-secondary"
                    on:click={() => Error_check()}>제출</button>

