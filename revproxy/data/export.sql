--
-- PostgreSQL database dump
--

-- Dumped from database version 9.6.10
-- Dumped by pg_dump version 9.6.10

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET client_min_messages = warning;
SET row_security = off;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: data; Type: TABLE; Schema: public; Owner: respoweb
--

CREATE TABLE public.data (
    id integer NOT NULL,
    categorie character varying,
    nom_domaine character varying,
    ip character varying,
    port character varying
);


ALTER TABLE public.data OWNER TO respoweb;

--
-- Name: data_id_seq; Type: SEQUENCE; Schema: public; Owner: respoweb
--

CREATE SEQUENCE public.data_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.data_id_seq OWNER TO respoweb;

--
-- Name: data_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: respoweb
--

ALTER SEQUENCE public.data_id_seq OWNED BY public.data.id;


--
-- Name: filename; Type: TABLE; Schema: public; Owner: respoweb
--

CREATE TABLE public.filename (
    id integer NOT NULL,
    nom_domaine character varying
);


ALTER TABLE public.filename OWNER TO respoweb;

--
-- Name: filename_id_seq; Type: SEQUENCE; Schema: public; Owner: respoweb
--

CREATE SEQUENCE public.filename_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.filename_id_seq OWNER TO respoweb;

--
-- Name: filename_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: respoweb
--

ALTER SEQUENCE public.filename_id_seq OWNED BY public.filename.id;


--
-- Name: data id; Type: DEFAULT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.data ALTER COLUMN id SET DEFAULT nextval('public.data_id_seq'::regclass);


--
-- Name: filename id; Type: DEFAULT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.filename ALTER COLUMN id SET DEFAULT nextval('public.filename_id_seq'::regclass);


--
-- Data for Name: data; Type: TABLE DATA; Schema: public; Owner: respoweb
--

COPY public.data (id, categorie, nom_domaine, ip, port) FROM stdin;
\.


--
-- Name: data_id_seq; Type: SEQUENCE SET; Schema: public; Owner: respoweb
--

SELECT pg_catalog.setval('public.data_id_seq', 1, false);


--
-- Data for Name: filename; Type: TABLE DATA; Schema: public; Owner: respoweb
--

COPY public.filename (id, nom_domaine) FROM stdin;
\.


--
-- Name: filename_id_seq; Type: SEQUENCE SET; Schema: public; Owner: respoweb
--

SELECT pg_catalog.setval('public.filename_id_seq', 1, false);


--
-- Name: data data_pkey; Type: CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.data
    ADD CONSTRAINT data_pkey PRIMARY KEY (id);


--
-- Name: filename filename_pkey; Type: CONSTRAINT; Schema: public; Owner: respoweb
--

ALTER TABLE ONLY public.filename
    ADD CONSTRAINT filename_pkey PRIMARY KEY (id);


--
-- PostgreSQL database dump complete
--

