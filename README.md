<p align="right"><b>English</b> · <a href="README.es.md">Español</a></p>

<p align="center">
  <img src="assets/banner.svg" alt="Eduardo Araque · Mathematician · Statistics · Data Science" width="100%">
</p>

<p align="center">
  <a href="https://www.linkedin.com/in/eduardo-araque-jacome-math"><img src="https://img.shields.io/badge/LinkedIn-Eduardo%20Araque-7A1F2B?logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="mailto:eduardoaraque06@hotmail.com"><img src="https://img.shields.io/badge/Email-eduardoaraque06%40hotmail.com-7A1F2B?logo=maildotru&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Open%20to-part--time%20%C2%B7%20freelance%20%C2%B7%20remote-4A0F17" alt="Open to part-time, freelance, remote">
</p>

## About me

I am a final-year **pure mathematics** student at Universidad Central del Ecuador who works where rigorous mathematics meets real data. My training (real and functional analysis, measure theory, numerical analysis, PDEs, mathematical statistics) is what I use to **check that an analysis is right**, not only that it runs.

- **Forecasting methodology for a national regulator.** During my internship at Ecuador's hydrocarbon regulatory agency I authored a 73-page forecasting and anomaly-detection methodology (SARIMAX with intervention analysis, proposed to replace the 2017 one), with its Python pipeline and user manuals.
- **Honest results.** I audit pipelines, fix what is wrong and report what does not work: in a rain-prediction project I corrected four critical preprocessing errors and documented that the model did not beat a simple baseline.
- **Verified numbers.** I re-derive what libraries compute: in my survey-sampling project, 98 out of 98 estimates from R's `survey` package were reproduced by hand.

## What I can help with

| Need | What I do | Tools |
|---|---|---|
| Survey and official data | Estimation with sampling weights, strata and clusters; correct standard errors, design effects, domain estimates | R (`survey`, tidyverse) |
| Forecasting and anomaly detection | SARIMA/SARIMAX, intervention analysis, prediction intervals, monitoring rules | Python (statsmodels), R |
| Predictive modeling | Leakage-free features, temporal validation, calibration, comparison against baselines | Python (scikit-learn, XGBoost) |
| Reproducible reporting | Analyses where every figure is traceable to code; reports and documentation | Quarto, LaTeX, Word, Git |
| Mathematical content and AI training | Proofs, problem design and review, step-by-step solutions in Spanish and English | LaTeX |

## Featured projects

<!-- PROJECTS:START · añadir una fila <tr> por cada dos proyectos nuevos -->
<table>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Eduardo0602/muestreo-complejo-ser-estudiante">Complex survey sampling</a></h3>
      <em>How wrong is an analysis that ignores the sampling design?</em><br><br>
      Ecuador's national student assessment (50,578 students): ignoring clustering understates standard errors 1.8 to 3.8 times; ignoring weights biases the mean by more than 10 points.<br><br>
      <code>R</code> <code>survey</code> <code>tidyverse</code>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Eduardo0602/eda-limpieza-defunciones-ecuador-pandas-sql">Messy-data EDA</a></h3>
      <em>What must be fixed before trusting an official registry?</em><br><br>
      Ecuador's 2021 death registry (107,648 records): 369,685 disguised missing values found and every cleaning decision justified.<br><br>
      <code>Python</code> <code>pandas</code> <code>SQL</code>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Eduardo0602/regresion-lineal-numpy-desde-cero">Linear regression from scratch</a></h3>
      <em>Can a plane predict how deep Ecuador's earthquakes are?</em><br><br>
      Existence and uniqueness of the minimizer proved; normal equations and gradient descent in NumPy, matching scikit-learn to 2.84e-13.<br><br>
      <code>Python</code> <code>NumPy</code> <code>optimization</code>
    </td>
    <td width="50%" valign="top">
      <h3><a href="https://github.com/Eduardo0602/algebra-lineal-visual-numpy">Visual linear algebra</a></h3>
      <em>What does a matrix do, geometrically?</em><br><br>
      Linear maps, eigenvalues and SVD from scratch; image compression and an algebraic and numerical proof that PCA is the SVD of centered data.<br><br>
      <code>Python</code> <code>NumPy</code> <code>SVD</code>
    </td>
  </tr>
</table>
<!-- PROJECTS:END -->

## Toolbox

<!-- SKILLS:START · añadir insignias en la fila que corresponda -->
**Languages** &nbsp;
<img src="https://img.shields.io/badge/R-7A1F2B?logo=r&logoColor=white" alt="R">
<img src="https://img.shields.io/badge/Python-7A1F2B?logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/SQL-7A1F2B?logo=sqlite&logoColor=white" alt="SQL">
<img src="https://img.shields.io/badge/LaTeX-7A1F2B?logo=latex&logoColor=white" alt="LaTeX">

**Statistics & ML** &nbsp;
<img src="https://img.shields.io/badge/survey-4A0F17" alt="survey">
<img src="https://img.shields.io/badge/statsmodels-4A0F17" alt="statsmodels">
<img src="https://img.shields.io/badge/scikit--learn-4A0F17?logo=scikitlearn&logoColor=white" alt="scikit-learn">
<img src="https://img.shields.io/badge/XGBoost-4A0F17" alt="XGBoost">

**Data** &nbsp;
<img src="https://img.shields.io/badge/tidyverse-9C3341?logo=tidyverse&logoColor=white" alt="tidyverse">
<img src="https://img.shields.io/badge/pandas-9C3341?logo=pandas&logoColor=white" alt="pandas">
<img src="https://img.shields.io/badge/NumPy-9C3341?logo=numpy&logoColor=white" alt="NumPy">

**Workflow** &nbsp;
<img src="https://img.shields.io/badge/Git-555555?logo=git&logoColor=white" alt="Git">
<img src="https://img.shields.io/badge/Quarto-555555?logo=quarto&logoColor=white" alt="Quarto">
<img src="https://img.shields.io/badge/Jupyter-555555?logo=jupyter&logoColor=white" alt="Jupyter">
<img src="https://img.shields.io/badge/Excel%20%C2%B7%20Power%20BI-555555" alt="Excel and Power BI">
<!-- SKILLS:END -->

## Why a pure mathematician

| Background (UCE coursework) | What it brings to data work |
|---|---|
| Measure theory I–II, probability theory | Knowing exactly what an estimator estimates and under which assumptions |
| Mathematical statistics, statistical inference, linear models | Sampling designs, likelihood, confidence intervals and tests done right |
| Linear algebra I–III | PCA, SVD, least squares and conditioning understood, not memorized |
| Real analysis I–V, functional analysis I–II, optimization | Convergence and optimization arguments behind machine learning |
| Numerical analysis I–IV | Stable computation: solving systems instead of inverting matrices, error control |
| PDEs I–IV, dynamical systems, mathematical modeling | Turning a physical or economic process into a model with explicit assumptions |
| Proof writing | Finding the hidden assumption that makes a result fail |

## Currently

<!-- NOW:START · actualizar cada mes -->
- Final year of the mathematics degree, taking Linear Models, Probability Theory, Optimization, Dynamical Systems, Mathematical Modeling.
- Adding bootstrap variance estimation and a Quarto report to the survey-sampling project.
- Open to **part-time or freelance remote work** in data science, statistics or math for AI training.
<!-- NOW:END -->

<details>
<summary><b>En español</b></summary>
<br>

Soy matemático (último semestre, Universidad Central del Ecuador) y trabajo donde la matemática rigurosa se encuentra con datos reales. En mis prácticas en la Agencia de Regulación y Control de Hidrocarburos elaboré una metodología de pronóstico y detección de anomalías basada en SARIMAX (propuesta para sustituir la de 2017); analizo datos en R y Python (encuestas con factor de expansión, series de tiempo, modelos predictivos) y verifico cada cifra antes de entregarla. Busco trabajo de medio tiempo o freelance remoto en ciencia de datos, estadística o entrenamiento de IA en matemática.

**[Leer el perfil completo en español](README.es.md)**

</details>

---

<p align="center"><sub>Portfolio <em>From Mathematician to Data Scientist</em> · it grows with every project</sub></p>
