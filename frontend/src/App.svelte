<script>
  import Router from 'svelte-spa-router'
  import Home from './routes/Home.svelte';
  import Detail from './routes/Detail.svelte';
  import QuestionCreate from './routes/QuestionCreate.svelte';
  import QuestionModify from './routes/QuestionModify.svelte';
  import UserCreate from './routes/UserCreate.svelte';
  import UserLogin from './routes/UserLogin.svelte';
  import AnswerModify from './routes/AnswerModify.svelte';
  import SymptonHome from './routes/SymptonHome.svelte';

  const routes = {
    '/' : Home,
    '/detail/:question_id' : Detail,
    '/question-modify/:question_id' : QuestionModify,
    '/question-create' : QuestionCreate,
    '/user-create' : UserCreate,
    '/user-login' : UserLogin,
    '/answer-modify/:answer_id' : AnswerModify,
    '/sympton-home' : SymptonHome, 
  }
</script>

<Router {routes}/>