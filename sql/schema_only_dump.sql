--
-- PostgreSQL database dump
--

\restrict FqZpHpH6bWh4vecEZ6TZmzTsf1V14scfGDmx1O170DiZPhj1apgb4fPDwN8YsLO

-- Dumped from database version 14.19 (Homebrew)
-- Dumped by pg_dump version 14.19 (Homebrew)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: dim_company; Type: TABLE; Schema: public; Owner: santhosh
--

CREATE TABLE public.dim_company (
    company_id integer NOT NULL,
    company_name text NOT NULL,
    ticker text,
    sector text
);


ALTER TABLE public.dim_company OWNER TO santhosh;

--
-- Name: dim_company_company_id_seq; Type: SEQUENCE; Schema: public; Owner: santhosh
--

CREATE SEQUENCE public.dim_company_company_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dim_company_company_id_seq OWNER TO santhosh;

--
-- Name: dim_company_company_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: santhosh
--

ALTER SEQUENCE public.dim_company_company_id_seq OWNED BY public.dim_company.company_id;


--
-- Name: dim_date; Type: TABLE; Schema: public; Owner: santhosh
--

CREATE TABLE public.dim_date (
    date_id integer NOT NULL,
    full_date date NOT NULL,
    year integer,
    quarter integer,
    month integer,
    month_name text,
    day integer
);


ALTER TABLE public.dim_date OWNER TO santhosh;

--
-- Name: dim_date_date_id_seq; Type: SEQUENCE; Schema: public; Owner: santhosh
--

CREATE SEQUENCE public.dim_date_date_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.dim_date_date_id_seq OWNER TO santhosh;

--
-- Name: dim_date_date_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: santhosh
--

ALTER SEQUENCE public.dim_date_date_id_seq OWNED BY public.dim_date.date_id;


--
-- Name: fact_financials; Type: TABLE; Schema: public; Owner: santhosh
--

CREATE TABLE public.fact_financials (
    fact_id integer NOT NULL,
    company_id integer,
    date_id integer,
    accounts_receivable numeric,
    assets numeric,
    assets_current numeric,
    cash numeric,
    gross_profit numeric,
    income_before_tax numeric,
    income_tax numeric,
    inc_dec_receivable numeric,
    inc_dec_other_receivable numeric,
    inventory numeric,
    liabilities numeric,
    liabilities_current numeric,
    net_cash_financing numeric,
    net_cash_investing numeric,
    net_cash_operating numeric,
    net_income numeric,
    operating_expenses numeric,
    operating_income numeric,
    rd_expense numeric,
    stockholders_equity numeric,
    full_date date
);


ALTER TABLE public.fact_financials OWNER TO santhosh;

--
-- Name: fact_financials_fact_id_seq; Type: SEQUENCE; Schema: public; Owner: santhosh
--

CREATE SEQUENCE public.fact_financials_fact_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.fact_financials_fact_id_seq OWNER TO santhosh;

--
-- Name: fact_financials_fact_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: santhosh
--

ALTER SEQUENCE public.fact_financials_fact_id_seq OWNED BY public.fact_financials.fact_id;


--
-- Name: dim_company company_id; Type: DEFAULT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.dim_company ALTER COLUMN company_id SET DEFAULT nextval('public.dim_company_company_id_seq'::regclass);


--
-- Name: dim_date date_id; Type: DEFAULT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.dim_date ALTER COLUMN date_id SET DEFAULT nextval('public.dim_date_date_id_seq'::regclass);


--
-- Name: fact_financials fact_id; Type: DEFAULT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.fact_financials ALTER COLUMN fact_id SET DEFAULT nextval('public.fact_financials_fact_id_seq'::regclass);


--
-- Name: dim_company dim_company_pkey; Type: CONSTRAINT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.dim_company
    ADD CONSTRAINT dim_company_pkey PRIMARY KEY (company_id);


--
-- Name: dim_company dim_company_ticker_key; Type: CONSTRAINT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.dim_company
    ADD CONSTRAINT dim_company_ticker_key UNIQUE (ticker);


--
-- Name: dim_date dim_date_pkey; Type: CONSTRAINT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.dim_date
    ADD CONSTRAINT dim_date_pkey PRIMARY KEY (date_id);


--
-- Name: fact_financials fact_financials_pkey; Type: CONSTRAINT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.fact_financials
    ADD CONSTRAINT fact_financials_pkey PRIMARY KEY (fact_id);


--
-- Name: fact_financials fact_financials_company_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: santhosh
--

ALTER TABLE ONLY public.fact_financials
    ADD CONSTRAINT fact_financials_company_id_fkey FOREIGN KEY (company_id) REFERENCES public.dim_company(company_id);


--
-- PostgreSQL database dump complete
--

\unrestrict FqZpHpH6bWh4vecEZ6TZmzTsf1V14scfGDmx1O170DiZPhj1apgb4fPDwN8YsLO

